from src.parser import parse_arg, extract_text_from_pdf
from src.chunking import chunk_by_char
from src.embedding import VectorStore


def main() -> None:
    arg = parse_arg()
    text = extract_text_from_pdf(arg.pdf_path)
    chunks = chunk_by_char(text)
    retriever = VectorStore(chunks)
    retriever.embedding_similarity()
    query = "What is the total amount of the invoice?"
    context = retriever.retrieve(query)
    print(f'retrieve result: {context}')



if __name__ == "__main__":
    main()
