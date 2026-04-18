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
from config import DOCS_DIR


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


@app.post("/ingest/directory")
def ingest_directory():
    docs_path = Path(DOCS_DIR)
    if not docs_path.exists():
        raise HTTPException(404, f"Docs directory not found: {DOCS_DIR}")

    files = list(docs_path.glob("**/*.md"))
    if not files:
        return {"message": "No markdown files found", "files": 0, "chunks": 0}

    total_chunks = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        chunks = chunker.chunk_markdown(text, f.name)
        if chunks:
            embeddings = embedder.embed([c["text"] for c in chunks])
            store.insert(chunks, embeddings)
            total_chunks += len(chunks)

    return {"message": f"Ingested {len(files)} file(s)", "files": len(files), "chunks": total_chunks}


@app.post("/ingest/file")
async def ingest_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".md"):
        raise HTTPException(400, "Only .md files are supported")

    text = (await file.read()).decode("utf-8")
    chunks = chunker.chunk_markdown(text, file.filename)
    if not chunks:
        raise HTTPException(400, "File appears to be empty")

    embeddings = embedder.embed([c["text"] for c in chunks])
    store.insert(chunks, embeddings)

    return {"message": f"Ingested {file.filename}", "chunks": len(chunks)}


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

    query_embedding = embedder.embed_query(req.query)
    hits = store.search(query_embedding)

    if not hits:
        context = "No relevant documents found in the knowledge base."
    else:
        context = "\n\n---\n\n".join(
            f"[Source: {h['source']}]\n{h['text']}" for h in hits
        )

    return StreamingResponse(
        llm.stream_response(req.query, context, req.history),
        media_type="text/plain",
    )
