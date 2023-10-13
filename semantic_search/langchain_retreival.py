from ClientDb import ClientDb
from chromadb.utils import embedding_functions
import pandas as pd
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceInstructEmbeddings
import chromadb
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA

#variables
path = "chromadb"
collection_name = 'interview_qa'

instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
persistent_client = chromadb.PersistentClient(path=path)
collection = persistent_client.get_or_create_collection("interview_qa")

vectordb = Chroma(
    client=persistent_client,
    collection_name="interview_qa",
    embedding_function=instructor_embeddings,
    collection_metadata={"hnsw:space": "cosine"}
)

query= 'what is overfitting?'
# docs = vectorstore.similarity_search(query, 3)
# print(docs)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})

print(retriever)

result = vectordb.max_marginal_relevance_search(query,k=3, fetch_k=4)

print(result)

#load model 
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

pipe = pipeline(
    "text2text-generation",
    model=model, 
    tokenizer=tokenizer, 
    max_length=512,
    temperature=0,
    top_p=0.95,
    repetition_penalty=1.15
)

local_llm = HuggingFacePipeline(pipeline=pipe)

# create the chain to answer questions 
qa_chain = RetrievalQA.from_chain_type(llm=local_llm, 
                                  chain_type="stuff", 
                                  retriever=retriever, 
                                  return_source_documents=True)

print(qa_chain)