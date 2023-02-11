import comtypes.client
import pdf2docx

def convert_ppt_to_docx(ppt_filename, docx_filename):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    presentation = powerpoint.Presentations.Open(ppt_filename)
    presentation.SaveAs(docx_filename, 16)
    presentation.Close()
    powerpoint.Quit()

def convert_pdf_to_docx(pdf_filename, docx_filename):
    pdf2docx.parse(pdf_filename, docx_filename)

print('Select an option:')
print('1. Convert a PowerPoint presentation to a Word document')
print('2. Convert a PDF file to a Word document')
option = input('Enter an option number: ')

if option == '1':
    ppt_filename = input('Enter the filename of the PowerPoint presentation: ')
    docx_filename = input('Enter the filename of the Word document to create: ')
    convert_ppt_to_docx(ppt_filename, docx_filename)
    print('Presentation converted to Word document successfully.')
elif option == '2':
    pdf_filename = input('Enter the filename of the PDF file: ')
    docx_filename = input('Enter the filename of the Word document to create: ')
    convert_pdf_to_docx(pdf_filename, docx_filename)
    print('PDF file converted to Word document successfully.')
else:
    print('Invalid option selected.')
