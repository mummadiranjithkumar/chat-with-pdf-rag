# 📄 LLM-Powered Document Copilot (RAG) — Resume Analysis System

An AI-powered application that allows users to upload PDF documents and interact with them using natural language.

This project uses Retrieval-Augmented Generation (RAG) with LangChain, FAISS, HuggingFace embeddings, and Llama 3 via Ollama to generate accurate, context-aware answers — fully locally without any paid APIs.

🚀 Features

Upload and process PDF documents

Semantic search using embeddings

Context-aware responses using Llama 3

Fully local execution (no API key required)

Fast document retrieval with FAISS

Source chunk display for transparency

🧠 Tech Stack

Python

Streamlit

LangChain

Ollama (Llama3:8B)

HuggingFace Sentence Transformers

FAISS

PyPDF

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/chat-with-pdf-rag.git
cd chat-with-pdf-rag
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Install & run Ollama

Download Ollama:

https://ollama.com

Pull the model:

ollama pull llama3:8b

Start Ollama:

ollama serve
5️⃣ Run the app
streamlit run app.py
💡 How It Works

PDF is loaded and split into chunks

Chunks are converted into embeddings

Stored in FAISS vector database

User query → similarity search

Relevant context → sent to Llama 3

Grounded answer is generated

📌 Requirements

Python 3.9+

Ollama running locally

🏷️ Project Type

LLM-Powered Document Q&A System using RAG (Fully Offline)

👨‍💻 Author

Your Name
Ranjith kumar Mummadi
