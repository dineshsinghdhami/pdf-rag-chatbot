# # PDF RAG Chatbot

An AI-powered PDF Question Answering application built with Python, Streamlit, LangChain, ChromaDB, Hugging Face Embeddings, and Groq LLM. The application uses Retrieval-Augmented Generation (RAG) to answer user questions based on uploaded PDF documents.

---

## # Project Status

### # Completed

- Created the project structure
- Set up a Python virtual environment
- Installed all required dependencies
- Built the Streamlit user interface
- Added PDF upload functionality
- Extracted text from uploaded PDF documents
- Refactored PDF processing into reusable utility modules
- Split PDF text into semantic chunks using LangChain
- Generated embeddings using Hugging Face Sentence Transformers
- Created an in-memory Chroma Vector Database
- Implemented semantic similarity search
- Integrated Groq LLM for answer generation
- Connected Retrieval-Augmented Generation (RAG) pipeline
- Displayed retrieved document sources
- Tested the complete application locally

---

## # Current Features

- Upload PDF documents
- Automatic PDF text extraction
- Intelligent document chunking
- Hugging Face embedding generation
- Chroma Vector Database
- Semantic similarity search
- AI-powered question answering using Groq
- Source chunk visualization
- Clean and modular project structure

---

## # Project Structure

```text
pdf-rag-chatbot/
│
├── data/
│
├── utils/
│   ├── pdf_utils.py
│   ├── text_utils.py
│   ├── embedding_utils.py
│   ├── vector_store_utils.py
│   └── llm_utils.py
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## # RAG Pipeline

```text
User Uploads PDF
        │
        ▼
Extract PDF Text
        │
        ▼
Split Text into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store Embeddings in ChromaDB
        │
        ▼
User Asks a Question
        │
        ▼
Semantic Similarity Search
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Groq LLM
        │
        ▼
Generate Final Answer
```

---

## # Technologies Used

- Python
- Streamlit
- PyPDF
- LangChain
- LangChain Text Splitters
- LangChain Chroma
- ChromaDB
- Hugging Face Sentence Transformers
- Groq API
- Python Dotenv

---

## # Installation

### 1. Clone the repository

```bash
git clone https://github.com/dineshsinghdhami/pdf-rag-chatbot.git
```

### 2. Open the project folder

```bash
cd pdf-rag-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

### 5. Install the required packages

```bash
python -m pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

### 7. Run the application

```bash
python -m streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## # Application Workflow

1. Upload a PDF document.
2. The application extracts all readable text.
3. The text is divided into semantic chunks.
4. Embeddings are generated for every chunk.
5. Chunks are stored inside Chroma Vector Database.
6. User asks a natural language question.
7. Semantic search retrieves the most relevant chunks.
8. Groq LLM generates the final answer using only the retrieved context.
9. Retrieved source chunks are displayed for transparency.

---

## # Example Questions

- What skills does the applicant have?
- What projects are mentioned?
- What programming languages are listed?
- What certifications does the candidate hold?
- Summarize this resume.
- What is the candidate's education?

---

## # Learning Outcomes

This project demonstrates understanding of:

- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search
- Chroma Vector Database
- LangChain Framework
- Prompt Engineering
- Streamlit Application Development
- Modular Python Programming
- Environment Variable Management
- LLM Integration

---

## # Future Improvements

- Persistent Chroma database
- Multiple PDF support
- Chat history
- Conversation memory
- Source citations with page numbers
- Better UI/UX
- Streaming LLM responses
- Docker support
- Cloud deployment
- User authentication
- PDF summarization
- Export chat history

---

## # Author

**Dinesh Singh Dhami**

Built as a personal learning project to understand Retrieval-Augmented Generation (RAG), vector databases, semantic search, and modern LLM application development.