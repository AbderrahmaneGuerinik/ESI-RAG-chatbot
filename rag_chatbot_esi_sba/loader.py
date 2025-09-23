from langchain_community.document_loaders import JSONLoader
from langchain_core.documents import Document
from typing import List
import logging


logging.basicConfig(level=logging.INFO)


class JsonLoader:
    """ Handles loading langchain documents from a JSON file """

    def __init__(self, file_path="../data/raw/ESI-SBA.json"):
        self.file_path = file_path
        """ 
        Initializes the JSON_Loader
        
        Args:
            file_path: the path of the JSON file    
        """

    def load_json(self) -> List[Document]:
        """Loads the JSON file as langchain documents"""

        loader = JSONLoader(
            file_path=self.file_path,
            jq_schema=".[]",
            content_key="content",
            metadata_func=lambda record, metadata: {
                "url": record.get("url"),
                **metadata,
            }
        )
        try:
            documents = loader.load()
        except Exception as e:
            logging.ERROR(f"Error loading {self.file_path}: {e}")
            return []
        logging.info(f"{len(documents)} documents loaded from {self.file_path}")
        return documents
