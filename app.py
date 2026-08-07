import streamlit as st

from utils.pdf_utils import extract_text_from_pdf


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

        extracted_text = extract_text_from_pdf(uploaded_file)

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

    st.info(
        "Please upload a PDF document to continue."
    )