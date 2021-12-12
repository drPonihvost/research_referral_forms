import os

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

from weasyprint import HTML




HTML(filename='table_template.html').write_pdf('weasyprint-test.pdf')