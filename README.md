# 📄 Chat with PDF using RAG (Gemini AI)

An AI-powered application that allows users to upload PDF documents and interact with them using natural language.

This project uses Retrieval-Augmented Generation (RAG) with Google Gemini, LangChain, and a vector database to generate accurate, context-aware answers from custom documents.

---

## 🚀 Features

- Upload and process PDF documents
- Semantic search using embeddings
- Context-aware responses using Gemini
- Fast document retrieval

---

## 🏗️ Tech Stack

- Python  
- LangChain  
- Google Generative AI (Gemini)  
- FAISS  
- PyPDF  
- dotenv  

---

## ⚙️ Installation

```bash
git clone https://github.com/mummadiranjithkumar/chat-with-pdf-rag.git
cd chat-with-pdf-rag
pip install -r requirements.txt


```

---

## 🔑 Environment Variables

Create a `.env` file and add:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
python app.py
```

---

## 🧠 How It Works

1. Load PDF  
2. Split into chunks  
3. Convert into embeddings  
4. Store in FAISS  
5. Retrieve relevant chunks  
6. Send to Gemini for answer  

---

## 👨‍💻 Author

Ranjith Kumar
