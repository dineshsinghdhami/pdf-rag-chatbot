import hashlib

import streamlit as st

from utils.pdf_utils import extract_documents_from_pdf
from utils.text_utils import split_documents_into_chunks
from utils.embedding_utils import generate_embeddings
from utils.vector_store_utils import (
    create_vector_store,
    search_vector_store,
)
from utils.llm_utils import stream_answer

def generate_file_hash(uploaded_file):
    """
    Generate a unique SHA-256 hash for an uploaded file.
    """

    file_bytes = uploaded_file.getvalue()

    return hashlib.sha256(file_bytes).hexdigest()

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# -------------------------------------------------
# Custom Styling
# -------------------------------------------------

st.markdown(
    """
    <style>

    .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 5rem;
    }

    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .main-subtitle {
        text-align: center;
        color: #888888;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    .document-status {
        text-align: center;
        padding: 0.65rem 1rem;
        border-radius: 10px;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
        font-size: 0.95rem;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }

    .section-label {
        font-size: 1.05rem;
        font-weight: 600;
        margin-top: 1.4rem;
        margin-bottom: 0.6rem;
    }

    div[data-testid="stChatMessage"] {
        border-radius: 14px;
        padding: 0.3rem 0.4rem;
        margin-bottom: 0.5rem;
    }

    div[data-testid="stFileUploader"] {
        border-radius: 12px;
    }

    div[data-testid="stExpander"] {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# -------------------------------------------------
# Session State
# -------------------------------------------------

if "processed_file_hashes" not in st.session_state:
    st.session_state.processed_file_hashes = []

if "documents" not in st.session_state:
    st.session_state.documents = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "embeddings" not in st.session_state:
    st.session_state.embeddings = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown(
    '<div class="main-title">📄 PDF RAG Chatbot</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="main-subtitle">
        Upload your documents and ask questions using AI-powered retrieval.
    </div>
    """,
    unsafe_allow_html=True,
)


# -------------------------------------------------
# Upload Section
# -------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload PDF documents",
    type=["pdf"],
    accept_multiple_files=True,
    help="You can upload multiple PDF files.",
)


# -------------------------------------------------
# Empty State
# -------------------------------------------------

if not uploaded_files:

    st.info(
        "👆 Upload one or more PDF documents to start."
    )

    st.stop()


uploaded_file_names = sorted(
    [
        uploaded_file.name
        for uploaded_file in uploaded_files
    ]
)
uploaded_file_hashes = sorted(
    [
        generate_file_hash(uploaded_file)
        for uploaded_file in uploaded_files
    ]
)


# -------------------------------------------------
# PDF Processing
# -------------------------------------------------

try:

    if (
    st.session_state.processed_file_hashes
    != uploaded_file_hashes
):

        with st.spinner(
            "Preparing your documents..."
        ):

            all_documents = []

            # ---------------------------------------------
            # Extract PDF pages
            # ---------------------------------------------

            for uploaded_file in uploaded_files:

                pdf_documents = (
                    extract_documents_from_pdf(
                        uploaded_file
                    )
                )

                all_documents.extend(
                    pdf_documents
                )


            # ---------------------------------------------
            # Validate content
            # ---------------------------------------------

            if not all_documents:

                st.error(
                    "No readable text was found "
                    "in the uploaded documents."
                )

                st.stop()


            # ---------------------------------------------
            # Create chunks
            # ---------------------------------------------

            chunks = split_documents_into_chunks(
                all_documents
            )


            # ---------------------------------------------
            # Generate embeddings
            # ---------------------------------------------

            embeddings = generate_embeddings(
                chunks
            )


            # ---------------------------------------------
            # Create vector database
            # ---------------------------------------------

            vector_store = create_vector_store(
                chunks
            )


            # ---------------------------------------------
            # Save session state
            # ---------------------------------------------

            st.session_state.processed_file_hashes = (
    uploaded_file_hashes
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

            # New documents = new conversation
            st.session_state.chat_history = []


    # -------------------------------------------------
    # Load Session Data
    # -------------------------------------------------

    documents = st.session_state.documents
    chunks = st.session_state.chunks
    vector_store = st.session_state.vector_store


    # -------------------------------------------------
    # Compact Document Status
    # -------------------------------------------------

    pdf_count = len(uploaded_files)
    page_count = len(documents)

    st.markdown(
        f"""
        <div class="document-status">
            ✅ <b>{pdf_count}</b> document(s) ready
            &nbsp;&nbsp;•&nbsp;&nbsp;
            {page_count} pages indexed
        </div>
        """,
        unsafe_allow_html=True,
    )


    # -------------------------------------------------
    # Uploaded Document Details
    # -------------------------------------------------

    with st.expander(
        "📚 View uploaded documents"
    ):

        for file_name in uploaded_file_names:

            st.write(
                f"📄 {file_name}"
            )


    # -------------------------------------------------
    # Chat Header
    # -------------------------------------------------

    header_col, clear_col = st.columns(
        [6, 1]
    )

    with header_col:

        st.markdown(
            '<div class="section-label">💬 Chat with your documents</div>',
            unsafe_allow_html=True,
        )

    with clear_col:

        if st.button(
            "Clear",
            help="Clear conversation",
            use_container_width=True,
        ):

            st.session_state.chat_history = []

            st.rerun()


    # -------------------------------------------------
    # Empty Chat State
    # -------------------------------------------------

    if not st.session_state.chat_history:

        st.caption(
            "Ask a question about the information "
            "inside your uploaded documents."
        )


    # -------------------------------------------------
    # Display Previous Messages
    # -------------------------------------------------

    for message in st.session_state.chat_history:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )


            # ---------------------------------------------
            # Display Saved Sources
            # ---------------------------------------------

            if (
                message["role"] == "assistant"
                and message.get("sources")
            ):

                source_count = len(
                    message["sources"]
                )

                with st.expander(
                    f"📚 {source_count} source(s)"
                ):

                    for source in message["sources"]:

                        st.caption(
                            f"📄 {source['file']} "
                            f"• Page {source['page']}"
                        )


    # -------------------------------------------------
    # Chat Input
    # -------------------------------------------------

    user_question = st.chat_input(
        "Ask a question about your PDFs..."
    )


    if user_question:

        # ---------------------------------------------
        # Save User Message
        # ---------------------------------------------

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": user_question,
            }
        )


        # ---------------------------------------------
        # Display User Message
        # ---------------------------------------------

        with st.chat_message(
            "user"
        ):

            st.markdown(
                user_question
            )


        # ---------------------------------------------
        # Retrieve Relevant Context
        # ---------------------------------------------

        with st.spinner(
            "Finding relevant information..."
        ):

            relevant_documents = (
                search_vector_store(
                    vector_store,
                    user_question,
                    k=3,
                )
            )


        

        # ---------------------------------------------
        # Build Source List
        # ---------------------------------------------

        sources = []

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

                sources.append(
                    {
                        "file": source,
                        "page": page,
                    }
                )

                seen_sources.add(
                    source_key
                )


        # ---------------------------------------------
        # Display AI Response
        # ---------------------------------------------

        with st.chat_message(
     "assistant"
     ):

         answer = st.write_stream(
        stream_answer(
            user_question,
            relevant_documents,
            st.session_state.chat_history,
        )
    )

    if sources:

        with st.expander(
            f"📚 {len(sources)} source(s)"
        ):

            for source in sources:

                st.caption(
                    f"📄 {source['file']} "
                    f"• Page {source['page']}"
                )


        # ---------------------------------------------
        # Save Assistant Response
        # ---------------------------------------------

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": sources,
            }
        )


except Exception as error:

    st.error(
        f"Something went wrong: {error}"
    )