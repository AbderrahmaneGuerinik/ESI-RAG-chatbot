from fastapi import FastAPI
from pydantic import BaseModel
from .rag_chatbot import RAGChatbot

app = FastAPI()

chatbot = RAGChatbot()


class Query(BaseModel):
    question: str


@app.post("/ask")
def ask(query: Query):
    answer = chatbot.ask(query.question)
    return {"answer": answer}
