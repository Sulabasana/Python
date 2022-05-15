from PyPDF2 import PdfFileMerger

pdfs = ['PiotrFrydryszaMAHLE.pdf', 'PiotrFrydryszaMAHLE1.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("PiotrFrydryszakMAHLE.pdf")
merger.close()