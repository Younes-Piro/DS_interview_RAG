from ClientDb import ClientDb
from chromadb.utils import embedding_functions
import pandas as pd
from langchain.embeddings import HuggingFaceInstructEmbeddings

#variables
path = "chromadb"
collection_name = 'interview_qa'

#uses base model and cpu
ef = embedding_functions.InstructorEmbeddingFunction(model_name="hkunlp/instructor-xl") 

client = ClientDb(path, ef)
client.create_or_get_collection(collection_name)
print(f'collection created : {client.get_collection()}')


#query 
query= 'what is overfitting?'

results = client.search(query, 3)

print(results)

