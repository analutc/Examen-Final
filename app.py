import streamlit as st
import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
import random

# Descargar recursos necesarios de nltk
nltk.download('punkt')

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

def generate_questions(text):
    sentences = sent_tokenize(text)
    questions = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 5:  # Crear preguntas solo para oraciones más largas
            word_to_blank = random.choice(words)
            question = sentence.replace(word_to_blank, "_____")
            questions.append((question, word_to_blank))
    return questions

def main():
    st.title("Generador de Preguntas de Repaso")
    st.write("Sube un archivo PDF y genera preguntas de repaso basadas en su contenido.")

    pdf_file = st.file_uploader("Subir PDF", type=["pdf"])

    if pdf_file is not None:
        text = extract_text_from_pdf(pdf_file)
        questions = generate_questions(text)

        st.write("### Preguntas Generadas:")
        for i, (question, answer) in enumerate(questions):
            st.write(f"**Pregunta {i+1}:** {question}")
            st.write(f"**Respuesta:** {answer}")
            st.write("---")

if __name__ == "__main__":
    main()
