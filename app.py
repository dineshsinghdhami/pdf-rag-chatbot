import streamlit as st
from pypdf import PdfReader


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

    try:
        pdf_reader = PdfReader(uploaded_file)

        extracted_text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

        st.subheader("Extracted Text")

        if extracted_text.strip():
            st.text_area(
                "PDF Content",
                extracted_text,
                height=400,
            )
        else:
            st.warning(
                "No readable text was found in this PDF."
            )

    except Exception as error:
        st.error(f"Error reading PDF: {error}")

else:
    st.info("Please upload a PDF document to continue.")