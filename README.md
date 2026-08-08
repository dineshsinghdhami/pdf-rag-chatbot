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
- Integrated ChromaDB as the vector database
- Added persistent Chroma vector storage
- Implemented semantic similarity search
- Integrated Groq LLM for answer generation
- Connected the complete Retrieval-Augmented Generation (RAG) pipeline
- Displayed retrieved document source chunks
- Added Streamlit session state
- Prevented unnecessary PDF reprocessing during the same session
- Reused extracted text, chunks, embeddings, and vector store
- Added environment variable support for secure API key handling
- Tested the complete application locally

---

## # Current Features

- Upload PDF documents
- Automatic PDF text extraction
- Intelligent document chunking
- Hugging Face embedding generation
- Persistent Chroma Vector Database
- Semantic similarity search
- AI-powered question answering using Groq
- Retrieved source chunk visualization
- Streamlit session-state caching
- Reuse of previously processed PDF data during a session
- Reduced unnecessary embedding regeneration
- Secure API key handling using `.env`
- Clean and modular Python project structure

---

## # Project Structure

```text
pdf-rag-chatbot/
│
├── chroma_db/
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

> `.env`, `.venv/`, and `chroma_db/` should be excluded from Git using `.gitignore`.

---

## # RAG Pipeline

```text
User Uploads PDF
        │
        ▼
Check Session State
        │
        ├── Already Processed
        │        │
        │        ▼
        │   Reuse Existing Data
        │
        └── New PDF
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
        Store in ChromaDB
                 │
                 ▼
        Save Processed Data
        in Session State
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
- Streamlit Session State

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

On Windows:

```bash
.venv\Scripts\activate
```

### 5. Install the required packages

```bash
python -m pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Do not commit your `.env` file to GitHub.

### 7. Run the application

```bash
python -m streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

## # Application Workflow

1. Upload a PDF document.
2. The application checks whether the PDF has already been processed during the current session.
3. If it is a new PDF, readable text is extracted using PyPDF.
4. The extracted text is divided into smaller overlapping chunks.
5. Hugging Face Sentence Transformers generate embeddings for the chunks.
6. The document chunks and embeddings are stored in ChromaDB.
7. Processed PDF data is stored in Streamlit session state.
8. Repeated interactions reuse the processed data instead of generating embeddings again.
9. The user asks a natural-language question.
10. ChromaDB performs semantic similarity search.
11. The most relevant document chunks are retrieved.
12. The question and retrieved context are sent to the Groq LLM.
13. The LLM generates an answer based on the retrieved PDF content.
14. Retrieved source chunks can be viewed for transparency.

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
- PDF text extraction
- Text chunking strategies
- Vector embeddings
- Semantic search
- Chroma vector databases
- Persistent vector storage
- Hugging Face embedding models
- LangChain framework
- Prompt engineering
- Groq LLM integration
- Streamlit application development
- Streamlit session state
- Application performance optimization
- Modular Python programming
- Environment variable management
- Secure API key handling

---

## # Future Improvements

- Multiple PDF support
- Identify PDFs using file hashes instead of filenames
- Load existing Chroma collections across new application sessions
- Separate vector collections for different documents
- Chat-style interface
- Chat history
- Conversation memory
- Source citations with PDF page numbers
- Better retrieval quality
- Better UI/UX
- Streaming LLM responses
- PDF summarization
- Reset/delete uploaded documents
- Export chat history
- Docker support
- Automated testing
- Cloud deployment
- User authentication

---

## # Author

**Dinesh Singh Dhami**

Built as a personal learning project to understand Retrieval-Augmented Generation (RAG), vector databases, semantic search, LLM integration, and the development of practical AI applications.