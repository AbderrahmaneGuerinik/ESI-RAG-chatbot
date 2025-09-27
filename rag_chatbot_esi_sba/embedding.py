import os
import numpy as np
from openai import OpenAI
from typing import List
import logging
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


class Embedder:
    def __init__(self, openai_api_key=openai_api_key, model="text-embedding-3-large"):
        self.openai_api_key = openai_api_key
        self.client = OpenAI(api_key=self.openai_api_key)
        self.model = model

    def vectorize(self, texts: List[str]) -> List[np.ndarray]:
        embeddings = []
        try:
            response = self.client.embeddings.create(
                input=texts,
                model=self.model
            )
            embeddings = [np.array(e.embedding) for e in response.data]
            logging.info("Embedding done successfully!")
        except Exception as e:
            logging.error(f"Error while applying embedding: {e}")
        return embeddings
