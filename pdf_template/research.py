from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

canvas = Canvas("research.pdf", pagesize=A4)
pdfmetrics.registerFont(TTFont('TNR', 'times.ttf'))
pdfmetrics.registerFont(TTFont('TNRB', 'timesbd.ttf'))
canvas.setFont('TNR', 14)

canvas.drawString(100, 100, "ЭКЦ МВД по Республике Хакасия")

canvas.showPage()

canvas.save()