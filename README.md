# AI PDF Q&A Web App
This is a Flask based **RAG** application. 

User uploads a PDF -> text is extracted -> converted to vectors (embeddings) -> stored in FAISS -> when user asks a question, the system finds the relevant sections and generates the answer using **Groq API (LLaMA 3.3 70B)**.

---

## Features
- PDF Text Extraction - **pdfplumber**
- Extract and split text into semantic chunks  
- Generate embeddings and store them in a **vector database (FAISS/ChromaDB)**  
- Use **retrieval-augmented generation (RAG)** to find relevant context  
- Ask natural questions and get accurate, context-aware answers  
- Flask backend with simple, clean REST API endpoints

This project follows a standard **RAG (Retrieve-Augment-Generate)** pipeline:

1. **PDF Upload**  
   The user uploads a PDF file through the web interface.  
   The backend extracts text using `PyMuPDF` or `pdfplumber`.

2. **Text Chunking**  
   To keep this project simple, I’ll assume that every word counts as a token.
   I know this isn’t perfectly accurate for LLMs, but for a small RAG project it’s more than enough.

   I’ll use NLTK for sentence tokenization.
   Then, I’ll build chunks by grouping sentences together based on word counts.
   Each chunk will contain roughly 500 words, and there will be a small overlap between chunks (around 80 words) to keep the context consistent.

   This approach keeps the pipeline simple and readable while still giving good retrieval quality for PDF-based question answering.

3. **Embeddings Generation**  
   Each chunk is converted into a **vector representation (embedding)** using a model like  
   `sentence-transformers/all-MiniLM-L6-v2` or OpenAI’s `text-embedding-ada-002`.

4. **Vector Store Creation**  
   The embeddings and their corresponding text chunks are stored in a **vector database**,  
   such as **FAISS** or **ChromaDB**, allowing for similarity search.

5. **Retrieval Step**  
   When the user asks a question, the app:
   - Converts the question into an embedding.
   - Searches the vector store for the most similar chunks.
   - Selects the top results as **context** for the model.

6. **Answer Generation (LLM)**  
   The retrieved context and the user’s question are sent to **GROQ API**,  
   which uses **LLaMA 3.3 70B** to generate a concise and accurate answer.


## Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Flask |
| AI Framework | LangChain |
| Vector Store | FAISS / ChromaDB |
| LLM API | GROQ (LLaMA 3.3 70B) |
| PDF Parsing | PyMuPDF or pdfplumber |
| Embeddings | sentence-transformers / OpenAI Embeddings |
| Frontend | HTML, CSS, JS, Bootstrap |

---

```bash
# 1 Clone the repository
git clone https://github.com/yourusername/ai-pdf-qa.git
cd ai-pdf-qa

# 2 Create a virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# 3 Install dependencies
pip install -r requirements.txt

# 4 Add your GROQ API key
export GROQ_API_KEY="your_api_key_here"

# 5 Run the app
python app.py