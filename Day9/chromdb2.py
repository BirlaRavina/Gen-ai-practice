import chromadb
import pprint
client = chromadb.Client()

collection = client.get_or_create_collection(name='chrom_collection')
collection.upsert(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

result = collection.query(
    query_texts= 'this is text for embedding'
)

pprint.pp(result)