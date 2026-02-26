import os

import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama


st.title("📄 Chat with PDF (Free & Local)")
st.write("Upload a PDF and then ask questions about its content. Everything runs locally.")


def build_vector_store(pdf_file) -> FAISS:
    temp_path = "temp.pdf"
    with open(temp_path, "wb") as f:
        f.write(pdf_file.read())

    loader = PyPDFLoader(temp_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    db = FAISS.from_documents(docs, embeddings)

    if os.path.exists(temp_path):
        os.remove(temp_path)

    return db


pdf = st.file_uploader("Upload your PDF", type="pdf")

if pdf is not None:
    if "last_pdf_name" not in st.session_state or st.session_state.get("last_pdf_name") != pdf.name:
        with st.spinner("Indexing PDF (this is done only once per file)..."):
            try:
                st.session_state["db"] = build_vector_store(pdf)
                st.session_state["last_pdf_name"] = pdf.name
            except Exception as e:
                st.error(f"Error while processing PDF: {e}")
                st.stop()

    db: FAISS = st.session_state.get("db")

    query = st.text_input("Ask a question about the PDF")

    if query:
        try:
            llm = Ollama(model="llama3:8b")

            # Manually perform retrieval + generation, no RetrievalQA dependency
            docs = db.similarity_search(query, k=4)
            context = "\n\n".join(d.page_content for d in docs)

            prompt = (
                "You are a helpful assistant answering questions about a PDF document.\n\n"
                f"Context from the document:\n{context}\n\n"
                f"Question: {query}\n\n"
                "Answer concisely and only using the information in the context. "
                "If the answer is not contained in the context, say you don't know."
            )

            answer = llm.invoke(prompt)

            st.subheader("Answer")
            st.write(answer)

            if docs:
                with st.expander("Show source chunks"):
                    for i, doc in enumerate(docs, start=1):
                        st.markdown(f"**Chunk {i}:**")
                        st.write(doc.page_content)
        except Exception as e:
            st.error(f"Error while generating answer: {e}")
