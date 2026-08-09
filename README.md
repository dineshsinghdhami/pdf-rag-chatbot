# # PDF RAG Chatbot

An AI-powered PDF Question Answering application that uses Retrieval-Augmented Generation (RAG) to answer questions from uploaded PDF documents.

Built with Python, Streamlit, LangChain, ChromaDB, Hugging Face Embeddings, and Groq LLM.

## # Features

- Upload multiple PDF documents
- Extract text page by page
- Split documents into semantic chunks
- Generate Hugging Face embeddings
- Store and retrieve documents using ChromaDB
- Semantic similarity search
- AI-powered answers using Groq
- Source filename and page number references
- Chat interface with conversation history
- Persistent Chroma vector database

## # RAG Pipeline

```text
PDF Upload
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

## # Technologies Used

- Python
- Streamlit
- LangChain
- PyPDF
- ChromaDB
- Hugging Face Sentence Transformers
- Groq API
- Python Dotenv

## # Project Structure

```text
pdf-rag-chatbot/
│
├── utils/
│   ├── pdf_utils.py
│   ├── text_utils.py
│   ├── embedding_utils.py
│   ├── vector_store_utils.py
│   └── llm_utils.py
│
├── chroma_db/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

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

## # Current Progress

The core RAG pipeline is working successfully.

Completed:

- Multiple PDF support
- PDF text extraction
- Document chunking
- Embedding generation
- Persistent ChromaDB
- Semantic search
- Groq LLM integration
- Source filename and page references
- Chat interface
- Chat history

## # Future Improvements

- Conversational memory
- Streaming responses
- Improved PDF preview
- Better document management
- Docker support
- Cloud deployment

## # Author

**Dinesh Singh Dhami**

Built as a personal learning project to understand Retrieval-Augmented Generation (RAG), vector databases, semantic search, and LLM application development.