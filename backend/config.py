import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# "google" → uses gemini-embedding-001 via API
# "local"  → uses sentence-transformers model on device
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "google")

GOOGLE_EMBEDDING_MODEL = "gemini-embedding-001"
LOCAL_EMBEDDING_MODEL = os.getenv("LOCAL_EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")

# Dimensions must match the chosen provider's model output
# gemini-embedding-001 → 3072 | bge-small-en-v1.5 → 384
_default_dim = "3072" if EMBEDDING_PROVIDER == "google" else "384"
EMBEDDING_DIM = int(os.getenv("EMBEDDING_DIM", _default_dim))

COLLECTION_NAME = "rag_docs"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
TOP_K = 5
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview")
DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs"))
