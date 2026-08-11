from langchain_chroma import Chroma

from utils.embedding_utils import get_embedding_model


CHROMA_DB_PATH = "./chroma_db"
COLLECTION_NAME = "pdf_documents"


def create_vector_store(chunks):
    """
    Create a fresh persistent Chroma vector store
    from LangChain Document chunks.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=CHROMA_DB_PATH,
    )

    vector_store.reset_collection()

    vector_store.add_documents(
        documents=chunks
    )

    return vector_store


def load_vector_store():
    """
    Load the existing persistent Chroma vector store.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=CHROMA_DB_PATH,
    )

    return vector_store


def search_vector_store(
    vector_store,
    query,
    k=5,
):
    """
    Search the vector database and return
    the most relevant document chunks.
    """

    results = vector_store.similarity_search(
        query=query,
        k=k,
    )

    return results


def search_vector_store_with_scores(
    vector_store,
    query,
    k=5,
):
    """
    Search the vector database and return
    documents together with similarity scores.
    """

    results = vector_store.similarity_search_with_score(
        query=query,
        k=k,
    )

    return results


def get_relevant_documents(
    vector_store,
    query,
    k=5,
    max_score=1.2,
):
    """
    Retrieve candidate chunks and remove weak matches.

    Lower Chroma distance scores are generally better.
    At least one result is returned when available.
    """

    scored_results = search_vector_store_with_scores(
        vector_store,
        query,
        k=k,
    )

    if not scored_results:
        return []

    relevant_documents = [
        document
        for document, score in scored_results
        if score <= max_score
    ]

    # Always keep the best result if filtering removed everything
    if not relevant_documents:
        relevant_documents = [
            scored_results[0][0]
        ]

    return relevant_documents