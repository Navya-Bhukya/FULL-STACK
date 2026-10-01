from sentence_transformers import SentenceTransformer

with open("fest_info.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(f"Your file has {len(text)} characters.")
print()
print("Sample text:",text[:200])

def chunk_text(text,chunk_size = 200, overlap = 50):
    chunks = []
    start = 0
    while start < len(text):overlap
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks

chunks = chunk_text(text)

model = SentenceTransformer('all-MiniLM-L6-V2')
embeddings = model.encode(chunks)

print(f"Total {len(chunks)} created-> Shape of embeddings: {embeddings.shape}")

for i in range(len(embeddings)):
    print(f"emb_{i+1}: {embeddings[i][:5]}")
    print()
    print("-------------------------------")