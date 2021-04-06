#! python3
# Main.py - enter folder path location and keyword or search term, this will read all pdfs in and add all the sentences that contains keyword into a txt file.
from pdf_format import PdfFormat

new_pdf = PdfFormat()
new_pdf.pdf_walk()