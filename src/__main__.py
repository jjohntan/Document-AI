from src.parser import parse_arg, extract_text_from_pdf
from src.chunking import chunk_by_char
from src.embedding import Retriever


def main() -> None:
    arg = parse_arg()
    text = extract_text_from_pdf(arg.pdf_path)
    chunks = chunk_by_char(text)
    retriever = Retriever()
    retriever.embedding_similarity(chunks)


if __name__ == "__main__":
    main()
