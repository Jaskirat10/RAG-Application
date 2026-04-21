from uuid import uuid4
import chromadb
from config import COLLECTION_NAME, TOP_K

_client = None
_collection = None


def get_collection():
    global _client, _collection
    if _collection is None:
        _client = chromadb.PersistentClient(path="./chroma_db")
        _collection = _client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )
    return _collection


def ensure_collection():
    get_collection()


def insert(chunks: list[dict], embeddings: list[list[float]]):
    col = get_collection()
    col.add(
        ids=[str(uuid4()) for _ in chunks],
        embeddings=embeddings,
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"]} for c in chunks],
    )


def search(query_embedding: list[float]) -> list[dict]:
    col = get_collection()
    results = col.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K,
        include=["documents", "metadatas", "distances"],
    )
    hits = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        hits.append({"text": doc, "source": meta["source"], "score": dist})
    return hits


def list_sources() -> list[str]:
    col = get_collection()
    results = col.get(include=["metadatas"])
    return sorted({m["source"] for m in results["metadatas"]})


def delete_collection():
    global _collection
    if _client:
        try:
            _client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass
        _collection = None
