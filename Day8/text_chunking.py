# Character-based Chunking

from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """A virtual environment is an isolated Python environment that allows you to manage dependencies for each project separately. 
It prevents conflicts between projects and avoids affecting the system-wide Python installation. Tools like venv or virtualenv are commonly used to create them.

Why do we need a Virtual Environment
Avoid Dependency Conflicts: Different projects may require different versions of the same library (e.g., Django 4.0 vs 4.1).
Isolate Project Environments: Keeps each project’s packages and settings separate from others and from the system Python.
Simplifies Project Management: Makes it easier to manage and replicate project-specific setups.
Prevents System Interference: Avoids accidentally modifying or breaking the global Python environment.
Enables Reproducibility: Ensures consistent behavior across development, testing and deployment environments.
When and Where to use a Virtual Environment?
"""
print(len(text))
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1,
    chunk_overlap = 0,
    # separators= ''
)
para_splitting = RecursiveCharacterTextSplitter(
    separators= ['\n\n', '\n', " ", ""],
    chunk_size = 100,
    chunk_overlap = 20
)
chunks = splitter.split_text(text)
para = para_splitting.split_text(text)

for chunk in chunks:
    print(chunk)
    print()

print('________________+++++++++++++++++___________________')
for p in para:
    print(p)
    print('-------------')
