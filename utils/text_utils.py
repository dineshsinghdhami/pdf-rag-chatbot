from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents_into_chunks(documents):
    """
    Split LangChain Document objects into smaller chunks
    while preserving metadata such as source filename
    and page number.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )

    chunks = text_splitter.split_documents(
        documents
    )

    return chunks