from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(text: str) -> list[dict]:
    """
    Split resume text into semantically meaningful chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100,
        separators=[
            "\n\n",      # Section / paragraph
            "\n",        # New line
            ". ",        # Sentence
            ", ",        # Phrase
            " ",         # Word
            ""           # Character fallback
        ],
        length_function=len,
        is_separator_regex=False,
    )

    chunks = splitter.split_text(text)

    return [
        {
            "chunk_id": index,
            "text": chunk,
        }
        for index, chunk in enumerate(chunks)
    ]
