from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

content = [
    'Delhi is city',
    'Delhi is capital of india',
    'India is a Country'
]
query = 'In which country is  Delhi located'

pairs = [(query, con) for con in content]
score = reranker.predict(pairs)
scored_data = [x for _, x in sorted(zip(score, content), reverse= True)]

print(scored_data[0])