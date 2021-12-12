from jinja2 import Environment, FileSystemLoader
import pdfkit

name = 'User'

options = {
    'page-size': 'A4',
    'margin-top': '37mm',
    'margin-right': '20mm',
    'margin-bottom': '15mm',
    'margin-left': '20mm',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [],
    'no-outline': None
}

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("table_template.html")

pdf_template = template.render({'name': name})

pdfkit.from_string(pdf_template, 'out.pdf', options=options)