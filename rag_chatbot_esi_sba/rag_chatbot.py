from llm_generator import LLMGenerator
from vector_store import VectorStore
from embedding import Embedder
from loader import JsonLoader

loader = JsonLoader(file_path="../data/raw/ESI-SBA.json")
vector_store = VectorStore()
llm = LLMGenerator()

documents = loader.load_json()
texts = [doc.page_content for doc in documents]

# load the faiss index
vector_store.load_index(path="../data/vectorstore/index.faiss")


class RAGChatbot:
    """ Combines the full RAG pipeline """

    def __init__(self, documents, llm=llm, texts=texts):
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
        context = self.texts[int(I[0][0])]
        llm_response = self.llm.generate(query=query, context=context)
        return llm_response
