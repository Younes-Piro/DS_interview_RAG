import pandas as pd
from InstructorEmbedding import INSTRUCTOR
from langchain.embeddings import HuggingFaceInstructEmbeddings
import chromadb
from chromadb.utils import embedding_functions

# import our dataset
df = pd.read_csv("assets/final_result.csv", index_col=[0])

ids = []
list_elements = []

# create the elements to store
for i, row in df.iterrows():
    list_elements.append(f"question: {row['Question']}\nanswer: {row['Answer']}")
    ids.append(f"id{i+1}")


#uses base model and cpu
ef = embedding_functions.InstructorEmbeddingFunction() 


#itilialise chromadb client
client = chromadb.PersistentClient(path="chromadb")

#create the collection 
collection = client.get_or_create_collection(
    name="interview_qa",
    embedding_function=ef,
    metadata={"hnsw:space": "cosine"}
)

#add the element to the collection
collection.add(
    documents=list_elements,
    ids=ids
)

print(collection)


'''
    1. after loading create a list with question and answers
    2. creating chromaDB collection and add the list created
    3. create retreive similar question to retreive the most similar questions
    4. this question retreived pass to the context for the LLM and make the inference


'''