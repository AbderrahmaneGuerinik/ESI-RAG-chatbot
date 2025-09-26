from rag_chatbot_esi_sba.rag_chatbot import RAGChatbot

# chatbot
chatbot = RAGChatbot()
answer = chatbot.ask("Ou se trouve ESI-SBA")
print(answer)
