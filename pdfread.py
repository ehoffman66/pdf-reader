import pdfplumber
with pdfplumber.open(r'formsample.pdf') as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())
    print(len(pdf.pages))
