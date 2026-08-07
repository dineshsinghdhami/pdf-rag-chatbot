import streamlit as st

from utils.pdf_utils import extract_text_from_pdf
from utils.text_utils import split_text_into_chunks


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

        # Step 1: Extract text from the uploaded PDF
        extracted_text = extract_text_from_pdf(uploaded_file)

        if extracted_text.strip():

            st.subheader("PDF Processing")

            st.success("Text extracted successfully.")

            # Step 2: Split extracted text into chunks
            chunks = split_text_into_chunks(extracted_text)

            st.write(f"Total text chunks created: {len(chunks)}")

            # Show extracted text
            with st.expander("View Extracted PDF Text"):

                st.text_area(
                    "PDF Content",
                    extracted_text,
                    height=300,
                )

            # Show a few chunks for testing
            with st.expander("View Text Chunks"):

                for index, chunk in enumerate(chunks[:3]):

                    st.markdown(
                        f"### Chunk {index + 1}"
                    )

                    st.write(chunk)

                    st.divider()

        else:

            st.warning(
                "No readable text was found in this PDF."
            )

    except Exception as error:

        st.error(
            f"Error processing PDF: {error}"
        )

else:

    st.info(
        "Please upload a PDF document to continue."
    )