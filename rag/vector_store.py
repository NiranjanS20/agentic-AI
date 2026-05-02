import faiss
import numpy as np

class vectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []
    
    def add_embeddings(self, embeddings, chunks):
        self.index.add(np.array(embeddings).astype("float32"))
        self.chunks.extend(chunks)
    
    def search(self, query_embedding, top_k=3):
        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"), top_k
        )

        return [self.chunks[i] for i in indices[0] if i < len(self.chunks)]
