from ClientDb import ClientDb
from chromadb.utils import embedding_functions
import pandas as pd
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceInstructEmbeddings
import chromadb

#variables
path = "chromadb"
collection_name = 'interview_qa'

instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
persistent_client = chromadb.PersistentClient(path=path)
collection = persistent_client.get_or_create_collection("interview_qa")

vectorstore = Chroma(
    client=persistent_client,
    collection_name="interview_qa",
    embedding_function=instructor_embeddings,
    collection_metadata={"hnsw:space": "cosine"}
)

query= 'what is overfitting?'
docs = vectorstore.similarity_search(query, 3)
print(docs)
