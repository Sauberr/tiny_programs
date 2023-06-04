from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass
import environ

pdfwriter = PdfFileWriter()
pdf = PdfFileReader('your_pdf.pdf')

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Write your password: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)