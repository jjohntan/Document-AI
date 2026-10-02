from src.parse_pdf import parse_arg, extract_text_from_pdf


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
    extract_text_from_pdf(arg.filename)
    # chunk = chunk_by_char('This year out company engaged in many areas of research.  ##Section 1: Medical Research  This year saw significant strides in our understanding of XDR-4/, a "bug" we not seen before.')
    # chunk = chunk_by_char('If text shorter than chunk size')
    # chunk  = chunk_by_char('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu')
    # print(chunk)


if __name__ == "__main__":
    main()
