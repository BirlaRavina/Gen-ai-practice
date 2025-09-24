# similarity search using dense embedding/ cosine similarity(dense semantic search)
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/multi-qa-MiniLM-L6-cos-v1")

sentences = [
    "The cat sat on the mat.",
    "Dogs are loyal and friendly animals.",
    "A quick brown fox jumps over the lazy dog.",
    "Cats are known to be curious creatures.",
    "I went to the market to buy vegetables."
]

query = "Tell me something about cats."

qur_emb = model.encode(query)
doc_emb = model.encode(sentences)
# compute cosine similarity
scores = util.cos_sim(qur_emb, doc_emb)[0].cpu().tolist()
# using dot score
# scores = util.doc_score(qur_emb, doc_emb)[0].cpu().tolist()
doc_score_pairs = list(zip(sentences, scores))
doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)

# print(doc_score_pairs)
for sentence, score in doc_score_pairs:
    print(f"{score: .4f} {sentence}")