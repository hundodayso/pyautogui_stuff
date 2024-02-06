import img2pdf
import PyPDF2
from PIL import Image
import os



for filename in os.listdir():

    if filename.endswith('.jpg'):
        img = Image.open(filename)
        pdf_path = os.path.join( filename[:-4] + '.pdf')
        img.save(pdf_path, 'PDF', resolution=100.0)

pdf_merger = PyPDF2.PdfMerger()
for filename in os.listdir():
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(filename)
        pdf_merger.append(pdf_path)
pdf_merger.write(os.path.join('merged.pdf'))
#change the name "merged.pdf" into anyname, and add on the extension: ".pdf"
pdf_merger.close()
