from sentence_transformers import SentenceTransformer
import chromadb

print("Loading model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Connecting to ChromaDB...")

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    "telecom_rag"
)

query = "What is NGAP?"

print("\nQuestion:", query)

query_embedding = model.encode(
    query
).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

print("\nTop Retrieved Chunks:\n")

for i in range(len(results["documents"][0])):

    print(f"\n===== Rank {i+1} =====")

    print(
        "Source:",
        results["metadatas"][0][i]["source"]
    )

    print(
        "Chunk ID:",
        results["metadatas"][0][i]["chunk_id"]
    )

    print("\n")

    print(results["documents"][0][i][:1000])

    print("\n" + "-" * 80)