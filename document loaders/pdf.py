from langchain_community.document_loaders import PyPDFLoader
data=PyPDFLoader("document loaders/PrologTutorial.pdf")
docs=data.load()
print(len(docs))