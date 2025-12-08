import os, re, nltk
from typing import List, Dict
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

# Formatting and cleaning text

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

def Cleaner(s: str) -> str:
    s = s.replace("\u00AD", "")                 # soft hyphen
    s = re.sub(r"-\s*\n\s*", "", s)             # satır sonu tire birleştirme
    s = re.sub(r"[ \t]+\n", "\n", s)            # boşluk+newline sadeleştirme
    s = re.sub(r"\n{3,}", "\n\n", s)            # fazla boş satır
    return s.strip()

def Sentences(text: str) -> List[str]:
    sentences = nltk.tokenize.sent_tokenize(text)
    return sentences


DEĞİŞİKLŞİK

# Chunking functions

# I want to keep this project simple. So, I'll assume that every WORD is a token. I know this is not accurate, but for basic chunking it should be fine.
# Then, I will use nltk for sentence tokenization. Afterwards, I will build chunks based on word counts. BUT, the chunker will chunk sentences. 