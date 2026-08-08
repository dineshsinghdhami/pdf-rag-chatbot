import streamlit as st

from utils.pdf_utils import extract_text_from_pdf
from utils.text_utils import split_text_into_chunks
from utils.embedding_utils import generate_embeddings
from utils.vector_store_utils import (
    create_vector_store,
    search_vector_store,
)
from utils.llm_utils import generate_answer


st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="centered",
)

st.title("📄 PDF RAG Chatbot")

st.write(
    "Upload a PDF document and ask questions about its content."
)


# Initialize session state
if "processed_file_name" not in st.session_state:
    st.session_state.processed_file_name = None

if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "embeddings" not in st.session_state:
    st.session_state.embeddings = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None


uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
)


if uploaded_file is not None:

    st.success(
        f"Uploaded successfully: {uploaded_file.name}"
    )

    try:

        # Only process when a new PDF is uploaded
        if (
            st.session_state.processed_file_name
            != uploaded_file.name
        ):

            with st.spinner(
                "Processing PDF..."
            ):

                # Step 1: Extract PDF text
                extracted_text = extract_text_from_pdf(
                    uploaded_file
                )

                if not extracted_text.strip():
                    st.warning(
                        "No readable text was found in this PDF."
                    )

                    st.stop()

                # Step 2: Split text into chunks
                chunks = split_text_into_chunks(
                    extracted_text
                )

                # Step 3: Generate embeddings
                embeddings = generate_embeddings(
                    chunks
                )

                # Step 4: Create persistent vector store
                vector_store = create_vector_store(
                    chunks
                )

                # Save everything in session state
                st.session_state.processed_file_name = (
                    uploaded_file.name
                )

                st.session_state.extracted_text = (
                    extracted_text
                )

                st.session_state.chunks = (
                    chunks
                )

                st.session_state.embeddings = (
                    embeddings
                )

                st.session_state.vector_store = (
                    vector_store
                )

            st.success(
                "PDF processed successfully."
            )

        else:

            st.info(
                "Using previously processed PDF."
            )

        extracted_text = (
            st.session_state.extracted_text
        )

        chunks = (
            st.session_state.chunks
        )

        embeddings = (
            st.session_state.embeddings
        )

        vector_store = (
            st.session_state.vector_store
        )

        st.subheader(
            "PDF Processing"
        )

        st.write(
            f"Total text chunks created: {len(chunks)}"
        )

        st.write(
            f"Total embeddings created: {len(embeddings)}"
        )

        if embeddings:

            st.write(
                f"Embedding dimensions: {len(embeddings[0])}"
            )

        st.success(
            "Vector database ready."
        )

        st.divider()

        # Ask question
        st.subheader(
            "Ask a Question"
        )

        user_question = st.text_input(
            "Ask something about the uploaded PDF"
        )

        if user_question:

            with st.spinner(
                "Searching the document..."
            ):

                relevant_documents = search_vector_store(
                    vector_store,
                    user_question,
                    k=3,
                )

            with st.spinner(
                "Generating answer..."
            ):

                answer = generate_answer(
                    user_question,
                    relevant_documents,
                )

            st.subheader(
                "Answer"
            )

            st.write(
                answer
            )

            with st.expander(
                "View Retrieved Sources"
            ):

                for index, document in enumerate(
                    relevant_documents
                ):

                    st.markdown(
                        f"### Source {index + 1}"
                    )

                    st.write(
                        document.page_content
                    )

                    st.divider()

        with st.expander(
            "View Extracted PDF Text"
        ):

            st.text_area(
                "PDF Content",
                extracted_text,
                height=300,
            )

        with st.expander(
            "View Text Chunks"
        ):

            for index, chunk in enumerate(
                chunks[:3]
            ):

                st.markdown(
                    f"### Chunk {index + 1}"
                )

                st.write(
                    chunk
                )

                st.divider()

    except Exception as error:

        st.error(
            f"Error processing PDF: {error}"
        )

else:

    st.info(
        "Please upload a PDF document to continue."
    )