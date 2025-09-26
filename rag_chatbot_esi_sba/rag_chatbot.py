from .llm_generator import LLMGenerator
from .vector_store import VectorStore
from .embedding import Embedder
from .loader import JsonLoader
import numpy as np
import logging
from pathlib import Path

BASE_DIR = Path(__file__).parent


loader = JsonLoader(file_path=BASE_DIR.parent / "data" / "raw" / "ESI-SBA.json")

llm = LLMGenerator()

documents = loader.load_json()
texts = [doc.page_content for doc in documents]

# embedder = Embedder()
# vectors = np.array(embedder.vectorize(texts))
# metadata = [doc.metadata for doc in documents]


vector_store = VectorStore()
# vector_store.add_embeddings(vectors=vectors, metadata=metadata)


# save the faiss index
# vector_store.save_index()

# load the faiss index
vector_store.load_index(path=str(BASE_DIR.parent / "data" / "vectorstore" / "index.faiss"))


class RAGChatbot:
    """ Combines the full RAG pipeline """

    def __init__(self, documents=documents, llm=llm, texts=texts):
        self.vector_store = vector_store
        self.llm = llm
        self.documents = documents
        self.texts = texts

    def ask(self, query):
        """ 
        returns the generated response by the LLM

        Args:
            query: the user's question
        """
        I, _, _ = self.vector_store.search(query=query)
        logging.info(f"Most similar index: {I[0][0]}")
        context = '\n'.join(self.texts[i] for i in I[0])
        logging.info(context)
        # context = self.texts[int(I[0][0])]
        llm_response = self.llm.generate(query=query, context=context)
        return llm_response
