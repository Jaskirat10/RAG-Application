from pymilvus import MilvusClient
from config import MILVUS_URI, COLLECTION_NAME, EMBEDDING_DIM, TOP_K

_client: MilvusClient | None = None


def get_client() -> MilvusClient:
    global _client
    if _client is None:
        _client = MilvusClient(MILVUS_URI)
    return _client


def ensure_collection():
    client = get_client()
    if not client.has_collection(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            dimension=EMBEDDING_DIM,
            enable_dynamic_field=True,
        )


def insert(chunks: list[dict], embeddings: list[list[float]]):
    client = get_client()
    data = [
        {"vector": emb, "text": chunk["text"], "source": chunk["source"]}
        for chunk, emb in zip(chunks, embeddings)
    ]
    client.insert(collection_name=COLLECTION_NAME, data=data)


def search(query_embedding: list[float]) -> list[dict]:
    client = get_client()
    results = client.search(
        collection_name=COLLECTION_NAME,
        data=[query_embedding],
        limit=TOP_K,
        output_fields=["text", "source"],
    )
    return [
        {
            "text": hit["entity"]["text"],
            "source": hit["entity"]["source"],
            "score": hit["distance"],
        }
        for hit in results[0]
    ]


def list_sources() -> list[str]:
    client = get_client()
    try:
        results = client.query(
            collection_name=COLLECTION_NAME,
            filter="",
            output_fields=["source"],
            limit=10000,
        )
        return sorted({r["source"] for r in results})
    except Exception:
        return []


def delete_collection():
    client = get_client()
    if client.has_collection(COLLECTION_NAME):
        client.drop_collection(COLLECTION_NAME)
