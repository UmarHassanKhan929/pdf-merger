import PyPDF2, os

pdfFiles = [] #array for pdf files to hold
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfWriter = PyPDF2.PdfFileWriter() #create pdf writer object
    
for file in pdfFiles:
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    for page in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pdfWriter.addPage(pageObj)
    
pdfOutput = open('merged.pdf', 'wb') #first parameter name as you like
pdfWriter.write(pdfOutput)
pdfOutput.close()

