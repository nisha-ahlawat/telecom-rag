from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path

print("Loading model...")
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Connecting to ChromaDB...")
client = chromadb.Client()

# Delete old test collection
try:
    client.delete_collection("telecom_rag")
    print("Old collection deleted!")
except:
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

    chunk_files = sorted(
        chunk_dir.glob("*.txt")
    )

    print(f"\nProcessing {dataset}...")
    print(f"Chunks found: {len(chunk_files)}")

    for chunk_file in chunk_files:

        with open(chunk_file, "r", encoding="utf-8") as f:
            chunk_text = f.read()

        embedding = model.encode(chunk_text)

        chunk_id = f"{dataset}_{chunk_file.stem}"

        collection.add(
            documents=[chunk_text],
            embeddings=[embedding.tolist()],
            ids=[chunk_id],
            metadatas=[{"source": dataset}]
        )

        total_chunks += 1

        if total_chunks % 100 == 0:
            print(f"{total_chunks} chunks processed...")

print("\nEmbedding pipeline completed!")
print("Total chunks stored:", collection.count())