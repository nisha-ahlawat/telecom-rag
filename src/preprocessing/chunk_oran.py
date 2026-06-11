from pathlib import Path

input_file = Path("data/processed/oran_clean.txt")
output_dir = Path("data/chunks/oran")

output_dir.mkdir(parents=True, exist_ok=True)

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

chunk_size = 1000
overlap = 200

for i in range(0, len(text), chunk_size - overlap):

    chunk = text[i:i + chunk_size]

    chunk_file = output_dir / f"chunk_{i//(chunk_size - overlap) + 1}.txt"

    with open(chunk_file, "w", encoding="utf-8") as f:
        f.write(chunk)

print("Chunking completed!")