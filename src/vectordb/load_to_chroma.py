from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb
#This code takes a telecom chunk, converts it into an embedding (vector), and stores both the text and vector inside ChromaDB.
#
#chunk_1.txt
#     ↓
#Read text
#     ↓
#Generate embedding
#     ↓
#Store in ChromaDB

print("Loading model...")
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Connecting to ChromaDB...")
client = chromadb.Client()

collection = client.get_or_create_collection(
    name="telecom_rag"
)

chunk_file = Path(
    "data/chunks/38300/chunk_1.txt"
)

with open(chunk_file, "r", encoding="utf-8") as f:
    chunk_text = f.read()

print("Chunk loaded!")
print("Chunk length:", len(chunk_text))

embedding = model.encode(chunk_text)


embedding = model.encode(chunk_text)

print("Embedding created!")
print("Vector length:", len(embedding))

collection.add(
    documents=[chunk_text],
    embeddings=[embedding.tolist()],
    ids=["38300_chunk_1"]
)

print("Chunk stored in ChromaDB!")