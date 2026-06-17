from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path

print("Loading embedding model...")
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Connecting to ChromaDB...")

client = chromadb.PersistentClient(
    path="chroma_db"
)

# Delete old collection if it exists
try:
    client.delete_collection("telecom_rag")
    print("Old collection deleted!")
except Exception:
    print("No existing collection found.")

collection = client.get_or_create_collection(
    name="telecom_rag"
)

print("Fresh collection created!")

datasets = [
    "38300",
    "38331",
    "38413",
    "oran"
]

total_chunks = 0

for dataset in datasets:

    chunk_dir = Path(f"data/chunks/{dataset}")

    if not chunk_dir.exists():
        print(f"Directory not found: {chunk_dir}")
        continue

    chunk_files = sorted(chunk_dir.glob("*.txt"))

    print(f"\nProcessing {dataset}...")
    print(f"Chunks found: {len(chunk_files)}")

    for chunk_file in chunk_files:

        with open(chunk_file, "r", encoding="utf-8") as f:
            chunk_text = f.read()

        embedding = model.encode(chunk_text).tolist()

        chunk_id = f"{dataset}_{chunk_file.stem}"

        collection.add(
            ids=[chunk_id],
            documents=[chunk_text],
            embeddings=[embedding],
            metadatas=[
                {
                    "source": dataset,
                    "chunk_id": chunk_id
                }
            ]
        )

        total_chunks += 1

        if total_chunks % 100 == 0:
            print(f"{total_chunks} chunks processed...")

print("\nEmbedding pipeline completed!")
print("Total chunks stored:", collection.count())