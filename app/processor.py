import pdfplumber

def process_document(filepath):
    chunks = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for paragraph in text.split("\n\n"):
                    if len(paragraph) > 100:
                        chunks.append(paragraph.strip())
    return chunks
