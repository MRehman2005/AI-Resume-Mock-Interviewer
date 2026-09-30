from langchain_text_splitters import RecursiveCharacterTextSplitter
# Chunking the pdf file
def create_chunk(text):
    Spliting_text = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    )

    chunks = Spliting_text.split_text(text)

    return chunks
