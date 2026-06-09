from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The cat is sleeping",
    "A kitten is resting",
    "I love machine learning"
]

embeddings = model.encode(sentences)

query = "My pet cat"
query_embedding = model.encode([query])

similarities = cosine_similarity(
    query_embedding,
    embeddings
)

best_match_index = np.argmax(similarities)

print("Query:", query)
print()

for i, sentence in enumerate(sentences):
    print(
        sentence,
        "->",
        round(similarities[0][i], 3)
    )

print("\nMost Similar:")
print(sentences[best_match_index])