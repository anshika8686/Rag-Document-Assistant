from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=2)

data=TextLoader("document loaders/notes.txt")
docs=data.load()

chunks=text_splitter.split_documents(docs)
print(len(chunks))