import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
MILVUS_URI = os.getenv("MILVUS_URI", "./milvus_rag.db")
COLLECTION_NAME = "rag_docs"
EMBEDDING_MODEL = "models/text-embedding-004"
EMBEDDING_DIM = 768
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
TOP_K = 5
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-pro-preview-03-25")
DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs"))
