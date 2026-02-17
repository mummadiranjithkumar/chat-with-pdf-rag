import streamlit as st
import os
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain



# 🔐 LOAD API KEY
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# 🎨 UI
st.set_page_config(page_title="Chat with PDF")
st.header("📄 Chat with your PDF (FREE GEMINI)")

pdf = st.file_uploader("Upload your PDF", type="pdf")

if pdf:

    reader = PdfReader(pdf)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    # ✂️ SPLIT TEXT
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    # ✅ FREE EMBEDDING MODEL (WORKS WITH FREE KEY)
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    vector_store = FAISS.from_texts(chunks, embedding=embeddings)

    question = st.text_input("Ask a question from your PDF")

    if question:

        docs = vector_store.similarity_search(question)

        # ✅ FREE LLM MODEL
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.3
        )

        prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the provided context.

Context:
{context}

Question:
{input}
""")

        chain = create_stuff_documents_chain(llm, prompt)

        response = chain.invoke({
            "context": docs,
            "input": question
        })

        st.write("🤖 Answer:")
        st.write(response)
