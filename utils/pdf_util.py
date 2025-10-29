import pdfplumber
import os
from dotenv import load_dotenv
load_dotenv()


pdf_path = os.getenv("PDF_FOLDER")

def extract_text_from_pdf(file_path):
    texts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            texts.append(page.extract_text())
    return texts


def main():
    for filename in os.listdir(pdf_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(pdf_path, filename)
            texts = extract_text_from_pdf(file_path)
            print(f"Texts form for {filename}:")
            print(texts)

if __name__ == "__main__":
    main()