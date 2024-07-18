import io
import os
from docx import Document
from PyPDF2 import PdfReader

def convert_pdf_to_docx(pdf_path, docx_path):
    # Ouvrir le fichier PDF en mode binaire
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        # Lire le texte de chaque page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Créer un nouveau document Word
    doc = Document()
    # Ajouter le texte extrait du PDF au document Word
    doc.add_paragraph(text)

    # Enregistrer le document Word
    with io.open(docx_path, 'wb') as docx_file:
        doc.save(docx_file)

if __name__ == "__main__":
    pdf_path = "Delanno.pdf"
    docx_path = "Delanno.docx"
    convert_pdf_to_docx(pdf_path, docx_path)
