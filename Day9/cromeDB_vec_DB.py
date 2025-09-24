import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name='chrom_collection')

collection.add(
    ids= ['id1', 'id2'],
    documents=[
        'document one',
        'document two'
    ]
)

results = collection.query(
    query_texts=['this is query'],
    n_results=2
)

print(results)