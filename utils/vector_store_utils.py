from langchain_chroma import Chroma

from utils.embedding_utils import get_embedding_model


def create_vector_store(chunks):
    """
    Create a Chroma vector store from PDF text chunks.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embedding_model,
        collection_name="pdf_documents",
    )

    return vector_store