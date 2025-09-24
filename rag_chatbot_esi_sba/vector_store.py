import faiss
from typing import List
import numpy as np


class VectorStore:
    """ Store the vectors using faiss """

    def __init__(self, d: int = 3072):
        self.index = faiss.IndexFlatIP(d)
        self.metadata = []
        self.vectors = np.empty((0, d), dtype="float32")

    def add_embeddings(self, vectors: np.ndarray, metadata: List[dict]):
        """ 
        add embedding to the faiss index
        Args:
            vectors: numpy array of the the embeddings
        """
        self.index.add(vectors)
        self.vectors = np.vstack([self.vectors, vectors])
        self.metadata.extend(metadata)

    def search(self, query_vector, k=5):
        """ 
        search for the most k similar vectors
        Args:
            query_vector: the embedding
            k: number of similar vectors to return
        """
        D, I = self.index.search(query_vector, k)
        results_vecs = self.vectors[I]
        results_meta = [[self.metadata[j] for j in row] for row in I]
        return results_vecs, results_meta

    def save_index(self, path="../data/vectorstore/index.faiss"):
        """ write the index on disk """
        faiss.write_index(self.index, path)

    def load_index(self, path="../data/vectorstore/index.faiss"):
        """ read the index from disk """
        self.index = faiss.read_index(path)
