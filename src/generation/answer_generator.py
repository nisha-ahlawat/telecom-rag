# Telecom RAG Pipeline

# User Question
#      ↓
# Question Embedding
#      ↓
# ChromaDB Retrieval (Top-5 Chunks)
#      ↓
# Context Construction
#      ↓
# Groq Llama
#      ↓
# Answer + Sources

from sentence_transformers import SentenceTransformer
import chromadb

from llm import generate_answer

print("Loading embedding model...")

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

while True:

    question = input(
        "\nAsk a telecom question (or type 'exit'): "
    )

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    query_embedding = model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    print("\nGenerating answer...\n")

    answer = generate_answer(
        context=context,
        question=question
    )

    print("=" * 80)
    print("ANSWER")
    print("=" * 80)

    print(answer)

    print("\nSOURCES")

    for metadata in results["metadatas"][0]:
        print(
            f"- {metadata['chunk_id']}"
        )