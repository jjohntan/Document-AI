import argparse
import pymupdf


def  parse_arg() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='document-ai', 
        description='Extract text from PDF')
    parser.add_argument('filename', type=str, help='Please provide the PDF file')
    return parser.parse_args()


def  extract_text_from_pdf(file_name: str):
    doc = pymupdf.open(file_name) # open a document
    out = open("output.txt", "wb") # create a text output
    for page in doc: # iterate the document pages
        text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
        out.write(text) # write text of page
        out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    out.close()
    doc.close()