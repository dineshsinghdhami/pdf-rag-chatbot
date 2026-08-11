# # PDF RAG Chatbot

An AI-powered PDF Question Answering application built using Retrieval-Augmented Generation (RAG).

Upload multiple PDF documents, ask questions about their content, and receive AI-generated answers with source page references and retrieved text snippets.

## # Features

- Multiple PDF upload
- PDF text extraction and chunking
- Hugging Face embeddings
- ChromaDB vector storage
- Semantic similarity search
- Relevance-based retrieval filtering
- Groq LLM integration
- Streaming AI responses
- Conversational follow-up questions
- Chat history
- Source filename and page references
- Retrieved source snippets
- SHA-256 document identification

## # RAG Pipeline

```text
PDF Documents
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embeddings
      ↓
ChromaDB
      ↓
Semantic Search
      ↓
Relevant Context
      ↓
Groq LLM
      ↓
Answer + Sources
```

## # Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Hugging Face Sentence Transformers
- Groq
- PyPDF

## # Installation

Clone the repository:

```bash
git clone https://github.com/dineshsinghdhami/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run the application:

```bash
python -m streamlit run app.py
```

## # Project Structure

```text
pdf-rag-chatbot/
├── utils/
│   ├── pdf_utils.py
│   ├── text_utils.py
│   ├── embedding_utils.py
│   ├── vector_store_utils.py
│   └── llm_utils.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## # What I Learned

This project helped me gain hands-on experience with:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings and semantic search
- Vector databases
- LangChain document processing
- LLM integration
- Prompt engineering
- Conversational context
- Streaming LLM responses
- Building AI applications with Streamlit

## # Future Improvements

- Docker support
- Cloud deployment
- User authentication
- Advanced document management

## # Author

**Dinesh Singh Dhami**

Built as a hands-on project to understand and implement a complete Retrieval-Augmented Generation pipeline.