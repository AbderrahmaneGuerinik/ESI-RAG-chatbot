import os
from openai import OpenAI
from typing import List

openai_api_key = os.getenv("OPENAI_API_KEY")


class LLMGenerator:
    def __init__(self, api_key=openai_api_key):
        api_key = api_key
        self.client = OpenAI(api_key=api_key)

    def generate(self, query, context: str) -> str:
        """
        genrate the response by the LLM

        Args:
            query: the query
            context: the context (the most similar document in the db to the query) 
        """

        prompt = f""" 
            Utilise uniquement le contexte ci-dessous pour répondre à la question.
            Contexte :
            {context}
            
            Question:
            {query}
            """
        response = self.client.responses.create(
            model="gpt-5",
            input=[{
                "role": "user",
                "content": prompt
            }]
        )
        return response.output_text
