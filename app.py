import streamlit as st


st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="centered",
)

st.title("📄 PDF RAG Chatbot")

st.write(
    "Upload a PDF document and ask questions about its content."
)

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
)

if uploaded_file is not None:
    st.success(f"Uploaded successfully: {uploaded_file.name}")
else:
    st.info("Please upload a PDF document to continue.")