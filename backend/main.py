import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

import store
import embedder
import chunker
import llm
from config import DOCS_DIR, EMBEDDING_PROVIDER

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("rag")


@asynccontextmanager
async def lifespan(app: FastAPI):
    store.ensure_collection()
    yield


app = FastAPI(title="RAG Chat API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    query: str
    history: list[dict] = []


@app.get("/health")
def health():
    return {"status": "ok"}


def _ingest_chunks(chunks: list[dict]) -> int:
    import time
    total = 0

    if EMBEDDING_PROVIDER == "local":
        # Local model — no rate limits, embed all at once
        embeddings = embedder.embed([c["text"] for c in chunks])
        store.insert(chunks, embeddings)
        total = len(chunks)
        log.info(f"INGEST | Embedded and saved {total} chunks in one shot ✓")
    else:
        # Google API — batch with rate limit handling
        BATCH_SIZE = 20
        log.info(f"INGEST | {len(chunks)} chunks — processing in batches of {BATCH_SIZE}")
        for i in range(0, len(chunks), BATCH_SIZE):
            batch = chunks[i:i + BATCH_SIZE]
            while True:
                try:
                    embeddings = embedder.embed([c["text"] for c in batch])
                    store.insert(batch, embeddings)
                    total += len(batch)
                    log.info(f"INGEST | Saved batch {i // BATCH_SIZE + 1} ({len(batch)} chunks) ✓")
                    break
                except Exception as e:
                    if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                        log.warning("INGEST | Rate limit hit — waiting 65s...")
                        time.sleep(65)
                    else:
                        raise
            if i + BATCH_SIZE < len(chunks):
                time.sleep(13)

    return total


@app.post("/ingest/directory")
def ingest_directory():
    docs_path = Path(DOCS_DIR)
    if not docs_path.exists():
        raise HTTPException(404, f"Docs directory not found: {DOCS_DIR}")

    files = list(docs_path.glob("**/*.md"))
    if not files:
        return {"message": "No markdown files found", "files": 0, "chunks": 0}

    already_ingested = store.list_sources()
    total_chunks = 0

    for f in files:
        if f.name in already_ingested:
            log.info(f"SKIP | {f.name} already ingested")
            continue

        log.info(f"INGEST | Processing {f.name}")
        text = f.read_text(encoding="utf-8")
        chunks = chunker.chunk_markdown(text, f.name)
        if not chunks:
            continue

        total_chunks += _ingest_chunks(chunks)

    return {"message": f"Ingested {len(files)} file(s)", "files": len(files), "chunks": total_chunks}


@app.post("/ingest/file")
async def ingest_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".md"):
        raise HTTPException(400, "Only .md files are supported")

    if file.filename in store.list_sources():
        return {"message": f"{file.filename} already ingested — skipped", "chunks": 0}

    text = (await file.read()).decode("utf-8")
    chunks = chunker.chunk_markdown(text, file.filename)
    if not chunks:
        raise HTTPException(400, "File appears to be empty")

    total = _ingest_chunks(chunks)
    return {"message": f"Ingested {file.filename}", "chunks": total}


@app.get("/documents")
def list_documents():
    return {"sources": store.list_sources()}


@app.delete("/documents")
def clear_documents():
    store.delete_collection()
    store.ensure_collection()
    return {"message": "All documents cleared"}


@app.post("/chat")
def chat(req: ChatRequest):
    if not req.query.strip():
        raise HTTPException(400, "Query cannot be empty")

    log.info("─" * 60)
    log.info(f"USER QUERY: {req.query}")

    log.info("STEP 1 | Embedding query...")
    query_embedding = embedder.embed_query(req.query)
    log.info(f"STEP 1 | Done — vector dim: {len(query_embedding)}")

    log.info("STEP 2 | Searching ChromaDB...")
    hits = store.search(query_embedding)
    if hits:
        log.info(f"STEP 2 | Found {len(hits)} chunks:")
        for i, h in enumerate(hits, 1):
            log.info(f"         [{i}] source={h['source']} score={h['score']:.4f} | {h['text'][:80]}...")
    else:
        log.info("STEP 2 | No relevant chunks found")

    if not hits:
        context = "No relevant documents found in the knowledge base."
    else:
        context = "\n\n---\n\n".join(
            f"[Source: {h['source']}]\n{h['text']}" for h in hits
        )

    log.info("STEP 3 | Sending to Gemini and streaming response...")

    def stream_with_log():
        full = []
        for chunk in llm.stream_response(req.query, context, req.history):
            full.append(chunk)
            yield chunk
        log.info(f"STEP 3 | Done — {sum(len(c) for c in full)} chars returned")
        log.info("─" * 60)

    return StreamingResponse(stream_with_log(), media_type="text/plain")
