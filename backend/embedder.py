from config import (
    EMBEDDING_PROVIDER,
    GOOGLE_API_KEY,
    GOOGLE_EMBEDDING_MODEL,
    LOCAL_EMBEDDING_MODEL,
)

# ── lazy-loaded clients/models ──────────────────────────────────────────────
_google_client = None
_local_model = None


def _get_google_client():
    global _google_client
    if _google_client is None:
        from google import genai
        _google_client = genai.Client(api_key=GOOGLE_API_KEY)
    return _google_client


def _get_local_model():
    global _local_model
    if _local_model is None:
        from sentence_transformers import SentenceTransformer
        _local_model = SentenceTransformer(LOCAL_EMBEDDING_MODEL)
    return _local_model


# ── public API ───────────────────────────────────────────────────────────────

def embed(texts: list[str]) -> list[list[float]]:
    if EMBEDDING_PROVIDER == "local":
        model = _get_local_model()
        return model.encode(texts, normalize_embeddings=True).tolist()

    # Google provider
    client = _get_google_client()
    result = client.models.embed_content(
        model=GOOGLE_EMBEDDING_MODEL,
        contents=texts,
    )
    return [e.values for e in result.embeddings]


def embed_query(text: str) -> list[float]:
    if EMBEDDING_PROVIDER == "local":
        model = _get_local_model()
        return model.encode([text], normalize_embeddings=True)[0].tolist()

    # Google provider
    client = _get_google_client()
    result = client.models.embed_content(
        model=GOOGLE_EMBEDDING_MODEL,
        contents=text,
    )
    return result.embeddings[0].values
