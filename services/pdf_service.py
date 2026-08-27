from pypdf import PdfReader


def clean_text(text: str) -> str:
    return " ".join(text.split())

def extract_text (pdf_path)-> str :
    reader = PdfReader(pdf_path)
    full_text = ''
    for page in reader.pages:
        full_text += page.extract_text() + '\n'

    return clean_text(full_text)
