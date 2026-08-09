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
    "Upload one or more PDF documents and ask questions "
    "based on their content."
)


# -------------------------------------------------
# Session State
# -------------------------------------------------

if "processed_file_names" not in st.session_state:
    st.session_state.processed_file_names = []

if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "embeddings" not in st.session_state:
    st.session_state.embeddings = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None


# -------------------------------------------------
# Multiple PDF Upload
# -------------------------------------------------

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type=["pdf"],
    accept_multiple_files=True,
)


if uploaded_files:

    uploaded_file_names = sorted(
        [
            uploaded_file.name
            for uploaded_file in uploaded_files
        ]
    )

    st.success(
        f"{len(uploaded_files)} PDF file(s) uploaded successfully."
    )

    st.write("Uploaded files:")

    for uploaded_file in uploaded_files:
        st.write(f"- {uploaded_file.name}")

    try:

        # -------------------------------------------------
        # Check whether PDFs need processing
        # -------------------------------------------------

        if (
            st.session_state.processed_file_names
            != uploaded_file_names
        ):

            with st.spinner(
                "Processing PDF documents..."
            ):

                combined_text = ""

                # -----------------------------------------
                # Extract text from every uploaded PDF
                # -----------------------------------------

                for uploaded_file in uploaded_files:

                    pdf_text = extract_text_from_pdf(
                        uploaded_file
                    )

                    if pdf_text.strip():

                        combined_text += (
                            f"\n\n"
                            f"===== DOCUMENT: {uploaded_file.name} ====="
                            f"\n\n"
                        )

                        combined_text += pdf_text

                # -----------------------------------------
                # Check extracted text
                # -----------------------------------------

                if not combined_text.strip():

                    st.warning(
                        "No readable text was found "
                        "in the uploaded PDF files."
                    )

                    st.stop()

                # -----------------------------------------
                # Split combined text into chunks
                # -----------------------------------------

                chunks = split_text_into_chunks(
                    combined_text
                )

                # -----------------------------------------
                # Generate embeddings
                # -----------------------------------------

                embeddings = generate_embeddings(
                    chunks
                )

                # -----------------------------------------
                # Create vector database
                # -----------------------------------------

                vector_store = create_vector_store(
                    chunks
                )

                # -----------------------------------------
                # Save data in session state
                # -----------------------------------------

                st.session_state.processed_file_names = (
                    uploaded_file_names
                )

                st.session_state.extracted_text = (
                    combined_text
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
                "PDF documents processed successfully."
            )

        else:

            st.info(
                "Using previously processed PDF documents."
            )


        # -------------------------------------------------
        # Load saved session data
        # -------------------------------------------------

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


        # -------------------------------------------------
        # Processing Information
        # -------------------------------------------------

        st.subheader(
            "PDF Processing"
        )

        st.write(
            f"Total PDFs: {len(uploaded_files)}"
        )

        st.write(
            f"Total text chunks created: {len(chunks)}"
        )

        st.write(
            f"Total embeddings created: {len(embeddings)}"
        )

        if embeddings:

            st.write(
                f"Embedding dimensions: "
                f"{len(embeddings[0])}"
            )

        st.success(
            "Vector database ready."
        )

        st.divider()


        # -------------------------------------------------
        # Ask Question
        # -------------------------------------------------

        st.subheader(
            "Ask a Question"
        )

        user_question = st.text_input(
            "Ask something about the uploaded PDFs"
        )


        if user_question:

            # ---------------------------------------------
            # Semantic Search
            # ---------------------------------------------

            with st.spinner(
                "Searching the documents..."
            ):

                relevant_documents = (
                    search_vector_store(
                        vector_store,
                        user_question,
                        k=3,
                    )
                )

            # ---------------------------------------------
            # Generate Answer
            # ---------------------------------------------

            with st.spinner(
                "Generating answer..."
            ):

                answer = generate_answer(
                    user_question,
                    relevant_documents,
                )


            # ---------------------------------------------
            # Display Answer
            # ---------------------------------------------

            st.subheader(
                "Answer"
            )

            st.write(
                answer
            )


            # ---------------------------------------------
            # Show Retrieved Sources
            # ---------------------------------------------

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


        # -------------------------------------------------
        # View Combined Extracted Text
        # -------------------------------------------------

        with st.expander(
            "View Extracted PDF Text"
        ):

            st.text_area(
                "PDF Content",
                extracted_text,
                height=300,
            )


        # -------------------------------------------------
        # View First Three Chunks
        # -------------------------------------------------

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
            f"Error processing PDFs: {error}"
        )


else:

    st.info(
        "Please upload one or more PDF documents to continue."
    )