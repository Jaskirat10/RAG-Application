import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
col = client.get_collection("rag_docs")

print(f"Total chunks: {col.count()}")
print()

results = col.get(limit=10, include=["documents", "metadatas"])
for i, (doc, meta) in enumerate(zip(results["documents"], results["metadatas"]), 1):
    print(f"--- Record {i} ---")
    print(f"Source : {meta['source']}")
    print(f"Text   : {doc[:300]}")
    print()
