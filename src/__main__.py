from src.parse_pdf import parse_arg, extract_text_from_pdf
from src.embedding import embedding_similarity


def  chunk_by_char(text, chunk_size=150, chunk_overlap=20):
    chunks = []
    start_idx = 0
    
    while start_idx < len(text):
        end_idx = min(start_idx + chunk_size, len(text))
        print(f"start index: {start_idx} end index: {end_idx} length: {len(text)}")
        chunk_text = text[start_idx:end_idx]
        chunks.append(chunk_text)
        
        start_idx = (
            end_idx - chunk_overlap if end_idx < len(text) else len(text)
        )
    
    return chunks


def  main():
    arg = parse_arg()
    text = extract_text_from_pdf(arg.pdf_path)
    chunks = chunk_by_char(text)
    embedding_similarity(chunks)
    


if __name__ == "__main__":
    main()
