from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import pprint

loader = PyMuPDFLoader('/home/my/practice20August/Day5/Python (3).pdf')
docm = loader.load()
print(docm[0].page_content)

cont = CharacterTextSplitter(
    # separators= '',
    chunk_size = 400,
    chunk_overlap = 50

)

chunks = cont.split_documents(docm)

for chunk in chunks:
    pprint.pp(chunk.page_content)