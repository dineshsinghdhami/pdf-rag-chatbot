from langchain_chroma import Chroma

from utils.embedding_utils import get_embedding_model


CHROMA_DB_PATH = "./chroma_db"


def create_vector_store(chunks):
    """
    Create and persist a Chroma vector store
    from LangChain Document chunks.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name="pdf_documents",
        persist_directory=CHROMA_DB_PATH,
    )

    return vector_store


def load_vector_store():
    """
    Load an existing persistent Chroma vector store.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        collection_name="pdf_documents",
        embedding_function=embedding_model,
        persist_directory=CHROMA_DB_PATH,
    )

    return vector_store


def search_vector_store(
    vector_store,
    query,
    k=3,
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