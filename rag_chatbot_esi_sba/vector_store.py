import faiss
from typing import List
import numpy as np
import os
from openai import OpenAI
import pickle
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent


class VectorStore:
    """ Store the vectors using faiss """

    def __init__(self, d: int = 3072, model="text-embedding-3-large"):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.index = faiss.IndexFlatIP(d)
        self.metadata = []
        self.vectors = np.empty((0, d), dtype="float32")
        self.client = OpenAI(api_key=openai_api_key)
        self.model = model

    def add_embeddings(self, vectors: np.ndarray, metadata: List[dict]):
        """ 
        add embedding to the faiss index
        Args:
            vectors: numpy array of the the embeddings
        """
        self.index.add(vectors)
        self.vectors = np.vstack([self.vectors, vectors])
        self.metadata.extend(metadata)

    def search(self, query, k=5):
        """ 
        search for the most k similar vectors
        Args:
            query: the query
            k: number of similar vectors to return
        """
        response = self.client.embeddings.create(
            input=query,
            model=self.model
        )
        query_vector = np.array([response.data[0].embedding], dtype="float32")
        D, I = self.index.search(query_vector, k)
        results_meta = [[self.metadata[j] for j in row] for row in I]
        return I, results_meta, D

    def save_index(self, path=str(BASE_DIR.parent / "data" / "vectorstore" / "index.faiss")):
        """ write the index, vectors and metadata on disk """
        faiss.write_index(self.index, path)
        data = {
            "vectors": self.vectors,
            "metadata": self.metadata
        }
        with open(BASE_DIR.parent / "data" / "vectorstore" / "data.pkl", "wb") as f:
            pickle.dump(data, f)

    def load_index(self, path=str(BASE_DIR.parent / "data" / "vectorstore" / "index.faiss")):
        """ read the index, vectors and metadata from disk """
        self.index = faiss.read_index(path)
        with open(BASE_DIR.parent / "data" / "vectorstore" / "data.pkl", "rb") as f:
            data = pickle.load(f)
            self.vectors = data['vectors']
            self.metadata = data['metadata']
