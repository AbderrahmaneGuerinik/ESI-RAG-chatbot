# RAG Chatbot ESI-SBA

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This project is about a chatbot built using the RAG (Retrieval-Augmented Generation) technique. The chatbot can answer various questions about the Higher School of Computer Science of Sidi Bel Abbès (ESI-SBA), such as: Where is the school located? What courses are taught at the school? What opportunities are available after obtaining a diploma? What are the differences compared to ESI-Alger? and more.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── raw            <- The JSON file.
│   └── vectorstore    <- The faiss index.
│
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         rag_chatbot_esi_sba and configuration for tools like black
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── rag_chatbot_esi_sba   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes rag_chatbot_esi_sba a Python module
    │
    ├── api.py                  <- The endpoint api to ask the chatbot
    │
    ├── app.py                  <- The UI
    │
    ├── embedding.py            <- Code to create embeddings           
    │
    ├── llm_generator.py        <- Code to generate text from a query
    │
    ├── loader.py               <- Code to load JSON as langchain Documents
    │
    ├── rag_chatbot.py          <- The full RAG pipeline
    │
    └── vectore_store.py        <- Code relative to the vectorDB
```

## Data
The data was obtained by applying web scraping to the official school website (https://www.esi-sba.dz/fr/) using BeautifulSoup. This data is then stored as a JSON file in *data/raw/ESI-SBA.json*
Each element in the JSON file consists of a URL and its corresponding content: the URL indicates the page from which the data was scraped, and the content contains the text of that page.
The JSON file includes nearly all the information available on the official website (across all pages).

## Embedding
For semantic search and retrieval, this project uses the **`text-embedding-3-large`** model from OpenAI  
([documentation](https://platform.openai.com/docs/models/text-embedding-3-large)).  
This model produces embeddings of **dimension 3072**, which are used to represent text in a vector space for similarity search.

## Vecotr Database
To store and efficiently search embeddings, this project uses a **FAISS** index.  
FAISS allows fast similarity search in high-dimensional vector spaces, enabling retrieval of relevant documents based on their embeddings.

## LLM
To generate responses, this project uses the **GPT-5** model.  
The model takes user queries and, combined with the retrieval from the FAISS vector database, generates relevant and context-aware answers.

## Backend & Frontend
This project provides a **REST API backend** built with FastAPI, exposing endpoints to interact with the chatbot.  
The **frontend user interface** is built using Streamlit, allowing users to easily ask questions and view responses in a chat-like format.

## Deployment
The backend is deployed on Render.<br>
The frontend is deployed on streamlit cloud.

## Tech Stack
Python 3.11.13<br>
FAISS<br>
Numpy<br>
OpenAI API<br>
FastAPI<br>
Streamlit<br>
langchain<br>
BeautifulSoup & lxml<br>
uvicorn

## Usage
Here is the application link: https://esi-sba-chatbot.streamlit.app/

## Possible Future imporvments
- Use open-source models (instead of relying only on OpenAI.
- Enhance the user interface to make the chatbot more intuitive and engaging.
- Optimize response time.
- Keep data up to date by periodically re-scraping content from the school's official website.

--------

