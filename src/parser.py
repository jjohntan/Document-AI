import argparse
import pymupdf


def  parse_arg() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='Document Ai', 
        description='Extract text from PDF')
    parser.add_argument('pdf_path', type=str, help='Path to PDF file')
    return parser.parse_args()


def  extract_text_from_pdf(pdf_path: str) -> str:
    doc = pymupdf.open(pdf_path) # open a document
    pages = []

    with open("output.txt", "w", encoding="utf-8") as out:
        for page in doc: # iterate the document pages
            page_text = page.get_text()
            pages.append(page_text)
            out.write(page_text)
            out.write("\f") # page delimiter (form feed 0x0C)

    doc.close()
    return "\f".join(pages)