import os
from dotenv import load_dotenv
load_dotenv()


# Basic PDF text extraction
import pdfplumber
def extract_text_from_pdf(file_path):
    texts = []
    
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text() or ""
            if t.strip():
                texts.append(t)
    return "\n\n".join(texts)


# Chunking functions

# I want to keep this project simple. So, I'll assume that every WORD is a token. I know this is not accurate, but for basic chunking it should be fine.
# Then, I will use nltk for sentence tokenization. Afterwards, I will build chunks based on word counts. BUT, the chunker will chunk sentences. 