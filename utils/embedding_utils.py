from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Load and return the Hugging Face embedding model.
    """

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model


def generate_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """

    embedding_model = get_embedding_model()

    embeddings = embedding_model.embed_documents(chunks)

    return embeddings