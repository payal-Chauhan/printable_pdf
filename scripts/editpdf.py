from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

pdf_path = (
    Path.home()/"Desktop"/"PDF_project"/"files"/"security_and_privacy_of electronic_health_records.pdf"
)

pdf_reader= PdfFileReader(str(pdf_path))
pdf_writer_even=PdfFileWriter()
pdf_writer_odd = PdfFileWriter()


for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    if n%2==0:   #odd pages
        pdf_writer_odd.addPage(page)

with Path("rotated_odds.pdf").open(mode="wb") as output_file:
    pdf_writer_odd.write(output_file)




for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    if n%2!=0:   #even pages
        pdf_writer_even.addPage(page)




#writing my pdf down

with Path("rotated_evens.pdf").open(mode="wb") as output_file:
    pdf_writer_even.write(output_file)