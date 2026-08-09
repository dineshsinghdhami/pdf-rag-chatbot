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
    Generate embeddings for text chunks.

    Supports both:
    - plain text strings
    - LangChain Document objects
    """

    embedding_model = get_embedding_model()

    texts = []

    for chunk in chunks:

        if hasattr(chunk, "page_content"):
            texts.append(chunk.page_content)
        else:
            texts.append(str(chunk))

    embeddings = embedding_model.embed_documents(
        texts
    )

    return embeddings