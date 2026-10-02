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
    out = open("output.txt", "wb") # create a text output
    for page in doc: # iterate the document pages
        text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
        out.write(text) # write text of page
        out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    out.close()
    doc.close()
    return text