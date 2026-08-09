import streamlit as st

from utils.pdf_utils import extract_documents_from_pdf
from utils.text_utils import split_documents_into_chunks
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

if "documents" not in st.session_state:
    st.session_state.documents = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "embeddings" not in st.session_state:
    st.session_state.embeddings = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None


# -------------------------------------------------
# Upload PDFs
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
        st.write(
            f"- {uploaded_file.name}"
        )

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

                all_documents = []

                # -----------------------------------------
                # Extract page documents from PDFs
                # -----------------------------------------

                for uploaded_file in uploaded_files:

                    pdf_documents = (
                        extract_documents_from_pdf(
                            uploaded_file
                        )
                    )

                    all_documents.extend(
                        pdf_documents
                    )

                # -----------------------------------------
                # Check for readable content
                # -----------------------------------------

                if not all_documents:

                    st.warning(
                        "No readable text was found "
                        "in the uploaded PDF files."
                    )

                    st.stop()

                # -----------------------------------------
                # Split documents into chunks
                # -----------------------------------------

                chunks = split_documents_into_chunks(
                    all_documents
                )

                # -----------------------------------------
                # Generate embeddings for testing/statistics
                # -----------------------------------------

                chunk_texts = [
                    chunk.page_content
                    for chunk in chunks
                ]

                embeddings = generate_embeddings(
                    chunk_texts
                )

                # -----------------------------------------
                # Create vector database
                # -----------------------------------------

                vector_store = create_vector_store(
                    chunks
                )

                # -----------------------------------------
                # Save in session state
                # -----------------------------------------

                st.session_state.processed_file_names = (
                    uploaded_file_names
                )

                st.session_state.documents = (
                    all_documents
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
        # Load session data
        # -------------------------------------------------

        documents = (
            st.session_state.documents
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
        # Processing information
        # -------------------------------------------------

        st.subheader(
            "PDF Processing"
        )

        st.write(
            f"Total PDFs: {len(uploaded_files)}"
        )

        st.write(
            f"Total PDF pages extracted: {len(documents)}"
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
        # Ask question
        # -------------------------------------------------

        st.subheader(
            "Ask a Question"
        )

        user_question = st.text_input(
            "Ask something about the uploaded PDFs"
        )


        if user_question:

            # ---------------------------------------------
            # Semantic search
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
            # Generate answer
            # ---------------------------------------------

            with st.spinner(
                "Generating answer..."
            ):

                answer = generate_answer(
                    user_question,
                    relevant_documents,
                )


            # ---------------------------------------------
            # Display answer
            # ---------------------------------------------

            st.subheader(
                "Answer"
            )

            st.write(
                answer
            )


            # ---------------------------------------------
            # Display citations
            # ---------------------------------------------

            st.subheader(
                "Sources"
            )

            seen_sources = set()

            for document in relevant_documents:

                source = document.metadata.get(
                    "source",
                    "Unknown PDF",
                )

                page = document.metadata.get(
                    "page",
                    "Unknown",
                )

                source_key = (
                    source,
                    page,
                )

                if source_key not in seen_sources:

                    st.write(
                        f"📄 {source} — Page {page}"
                    )

                    seen_sources.add(
                        source_key
                    )


            # ---------------------------------------------
            # Retrieved source details
            # ---------------------------------------------

            with st.expander(
                "View Retrieved Source Content"
            ):

                for index, document in enumerate(
                    relevant_documents
                ):

                    source = document.metadata.get(
                        "source",
                        "Unknown PDF",
                    )

                    page = document.metadata.get(
                        "page",
                        "Unknown",
                    )

                    st.markdown(
                        f"### Source {index + 1}"
                    )

                    st.caption(
                        f"File: {source} | Page: {page}"
                    )

                    st.write(
                        document.page_content
                    )

                    st.divider()


        # -------------------------------------------------
        # View extracted pages
        # -------------------------------------------------

        with st.expander(
            "View Extracted PDF Pages"
        ):

            for index, document in enumerate(
                documents[:5]
            ):

                source = document.metadata.get(
                    "source",
                    "Unknown PDF",
                )

                page = document.metadata.get(
                    "page",
                    "Unknown",
                )

                st.markdown(
                    f"### {source} — Page {page}"
                )

                st.write(
                    document.page_content
                )

                st.divider()


        # -------------------------------------------------
        # View chunks
        # -------------------------------------------------

        with st.expander(
            "View Text Chunks"
        ):

            for index, chunk in enumerate(
                chunks[:3]
            ):

                source = chunk.metadata.get(
                    "source",
                    "Unknown PDF",
                )

                page = chunk.metadata.get(
                    "page",
                    "Unknown",
                )

                st.markdown(
                    f"### Chunk {index + 1}"
                )

                st.caption(
                    f"File: {source} | Page: {page}"
                )

                st.write(
                    chunk.page_content
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