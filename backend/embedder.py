import google.generativeai as genai
from config import GOOGLE_API_KEY, EMBEDDING_MODEL

genai.configure(api_key=GOOGLE_API_KEY)


def embed(texts: list[str], task_type: str = "retrieval_document") -> list[list[float]]:
    embeddings = []
    for text in texts:
        result = genai.embed_content(
            model=EMBEDDING_MODEL,
            content=text,
            task_type=task_type,
        )
        embeddings.append(result["embedding"])
    return embeddings


def embed_query(text: str) -> list[float]:
    result = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text,
        task_type="retrieval_query",
    )
    return result["embedding"]
