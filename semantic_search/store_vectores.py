from ClientDb import ClientDb
from chromadb.utils import embedding_functions
import pandas as pd
from langchain.embeddings import HuggingFaceInstructEmbeddings

#variables
path = "chromadb"
collection_name = 'interview_qa'

# import our dataset
df = pd.read_csv("assets/final_result.csv", index_col=[0])

ids = []
list_elements = []

# create the elements to store
for i, row in df.iterrows():
    list_elements.append(f"question: {row['Question']}\nanswer: {row['Answer']}")
    ids.append(f"id{i+1}")

#uses base model and cpu
ef = embedding_functions.InstructorEmbeddingFunction(model_name="hkunlp/instructor-xl") 
# instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")

client = ClientDb(path, ef)
client.create_or_get_collection(collection_name)
print(f'collection created : {client.get_collection()}')

client.store_vectores(list_elements, ids)

print("elements stored")


