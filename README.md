# # PDF RAG Chatbot

A beginner-friendly AI project that will allow users to upload PDF documents and ask questions based on their content using Retrieval-Augmented Generation (RAG).

## # Project Status

### # Completed Today

* Created the project folder
* Opened the project in Visual Studio Code
* Created a Python virtual environment
* Installed Streamlit and PyPDF
* Created the basic Streamlit interface
* Added a PDF upload feature
* Tested the application locally

## # Current Features

* Simple Streamlit user interface
* PDF file uploader
* PDF file type validation
* Upload success message
* Basic project structure

## # Project Structure

```text
pdf-rag-chatbot/
├── data/
├── utils/
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
└── .venv/
```

## # Technologies Used

* Python
* Streamlit
* PyPDF

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

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

## # Next Steps

* Extract text from uploaded PDF files
* Split PDF text into smaller chunks
* Generate text embeddings
* Store embeddings in a vector database
* Retrieve relevant document sections
* Connect the application to an LLM
* Display answers with source references

## # Author

Created as a beginner RAG learning project.
