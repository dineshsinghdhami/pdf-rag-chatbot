import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


# Force values from .env to replace older environment variables
load_dotenv(override=True)


def get_llm():
    """
    Create and return the Groq language model.
    """

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY was not found. Add it to your .env file."
        )

    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    return llm


def generate_answer(question, relevant_documents):
    """
    Generate an answer using the user's question
    and retrieved PDF context.
    """

    llm = get_llm()

    context = "\n\n".join(
        document.page_content
        for document in relevant_documents
    )

    prompt = f"""
You are a PDF question-answering assistant.

Answer the user's question using only the provided PDF context.

If the answer cannot be found in the context, say:
"I could not find the answer in the uploaded PDF."

Do not invent information.

PDF Context:
{context}

User Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content