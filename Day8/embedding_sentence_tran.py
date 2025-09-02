from sentence_transformers import SentenceTransformer, util

# model = SentenceTransformer("all-MiniLM-L6-v2")

# sentences = [
#     "The weather is lovely today.",
#     "It's so sunny outside!",
#     "He drove to the stadium.",
#     "the sun rises in the East"
# ]

# embeddings = model.encode(sentences)
# print(embeddings.shape)

# similarities = model.similarity(embeddings, embeddings)
# for i in similarities:
#     print(i)


# In which direction The sun is rises

model = SentenceTransformer("sentence-transformers/multi-qa-MiniLM-L6-cos-v1")

# query = "In which direction does The sun  rise"
query = "how is the weather today"
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
    "the sun rises in the East"
]

qur_emb = model.encode(query)
doc_emb = model.encode(sentences)

print("query ", qur_emb.shape)
print("doc", doc_emb.shape)

scores = util.dot_score(qur_emb, doc_emb)[0].cpu().tolist()
doc_score_pairs = list(zip(query, sentences))
doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)

print(doc_score_pairs)
