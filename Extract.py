from loader import load_pdf_file
DATA_PATH = "data/"
document = load_pdf_file(DATA_PATH)
# Extract Text from resume
def extract_text(document):
    text = ""
    for documents in load_pdf_file:
        text+=document.page_content
        text+='\n'

        return text
    