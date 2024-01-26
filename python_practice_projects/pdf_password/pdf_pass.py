from PyPDF2 import PdfWriter, PdfReader
import getpass
pdf_W =PdfWriter()
pdf_R =PdfReader("C:\\Users\\DHAARU\\Downloads\\SoP Rev4.pdf")
for page_number in range(len(pdf_R.pages)):
  pdf_W.add_page(pdf_R.pages[page_number])
password=getpass.getpass(prompt= "Enter the Password: ")  
pdf_W.encrypt(password)
with open("C:\\Users\\DHAARU\\Documents\\python_projects\\pdf_password\\SoP_Rev4.pdf",'wb') as file:
  pdf_W.write(file)
#password:dhaarusop@25














