import chromadb

class ClientDb:

    def __init__(self, path, ef):
        self.client = chromadb.PersistentClient(path=path)
        self.collection = any
        self.ef = ef

    
    def create_or_get_collection(self, name):
        #create the collection 
        self.collection = self.client.get_or_create_collection(
            name=name,
            embedding_function=self.ef,
            metadata={"hnsw:space": "cosine"}
        )
        

    def store_vectores(self, list_elements, ids):
        self.collection.add(
            documents=list_elements,
            ids=ids
        )
        

    def search(self, query, n_results):
        
        results = self.collection.query(
            query_texts=query,
            n_results=n_results
        )

        return results['documents'][0]

    def get_collection(self):
        return self.collection