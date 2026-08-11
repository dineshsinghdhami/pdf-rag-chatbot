import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


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


def generate_answer(
    question,
    relevant_documents,
    chat_history=None,
):
    """
    Generate an answer using:
    - the current question
    - retrieved PDF context
    - recent conversation history
    """

    llm = get_llm()

    context = "\n\n".join(
        document.page_content
        for document in relevant_documents
    )

    conversation = ""

    if chat_history:

        recent_messages = chat_history[-6:]

        for message in recent_messages:

            role = message.get(
                "role",
                "user",
            )

            content = message.get(
                "content",
                "",
            )

            conversation += (
                f"{role.capitalize()}: "
                f"{content}\n"
            )

    prompt = f"""
You are a PDF question-answering assistant.

Answer using only the provided PDF context.

Use the conversation history only to understand
follow-up references such as:
"that", "it", "the second one", or "tell me more".

Do not use conversation history as a source of factual
information unless that information is also supported
by the PDF context.

If the answer cannot be found in the PDF context, say:
"I could not find the answer in the uploaded PDF."

Do not invent information.

Conversation History:
{conversation}

PDF Context:
{context}

Current Question:
{question}

Answer:
"""

    response = llm.invoke(
        prompt
    )

    return response.content