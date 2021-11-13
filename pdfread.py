#!/usr/bin/env python

import pdfplumber

with pdfplumber.open(r'sample.pdf') as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())
    print("Number of Pages " + str(len(pdf.pages)))
