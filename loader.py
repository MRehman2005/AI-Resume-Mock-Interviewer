from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


def load_pdf_file(data):

    data_path = Path(data)

    # Check if directory exists
    if not data_path.exists():
        print("Data directory does not exist.")
        return []

    # Check if it is actually a directory
    if not data_path.is_dir():
        print("The given path is not a directory.")
        return []

    # Check if PDF files exist
    pdf_files = list(data_path.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return []

    # Load PDFs
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()

    print(f"{len(pdf_files)} PDF file(s) found.")
    print("Documents loaded successfully.")

    return documents

