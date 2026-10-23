from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders import PyPDFLoader
text_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=0)


data=PyPDFLoader("document loaders/PrologTutorial.pdf")
docs=data.load()

chunks = text_splitter.split_text(docs)
print(len(chunks))
