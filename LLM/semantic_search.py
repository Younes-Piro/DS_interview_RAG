import chromadb
from chromadb.utils import embedding_functions
import re

#itilialise chromadb client
client = chromadb.PersistentClient(path="chromadb")

#uses base model and cpu
ef = embedding_functions.InstructorEmbeddingFunction() 

collection = client.get_collection(name="interview_qa", embedding_function=ef)

query = "what is data science"

results = collection.query(
    query_texts=query,
    n_results=3
)

print(results['documents'][0][0])
