from pathlib import Path

input_file = Path("data/processsed/38300_clean.txt") #Open the cleaned telecom document
output_dir = Path("data/chunks/38300")

output_dir.mkdir(parents=True, exist_ok=True)

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

chunk_size = 1000  # Each chunk will contain 1000 characters.

for i in range(0, len(text), chunk_size):     #Creates files like: chunk_1.txt , chunk_2.txt , chunk_3.txt
    chunk = text[i:i + chunk_size]

    chunk_file = output_dir / f"chunk_{i//chunk_size + 1}.txt"

    with open(chunk_file, "w", encoding="utf-8") as f:
        f.write(chunk)

print("Chunking completed!")