import sys

from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets

# sys.argv.append("--disable-web-security")
from PySide6.QtCore import QMarginsF
from PySide6.QtGui import QPageLayout, QPageSize

name = 'User'

app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()
loader.setZoomFactor(1)
loader.pdfPrintingFinished.connect(
    lambda *args: print('finished:', args))
loader.load(QtCore.QUrl('file:///research_template.html'))


def emit_pdf(finished):
    loader.show()
    param = QPageLayout(QPageSize(QPageSize.A4), QPageLayout.Portrait, QMarginsF())
    param.setUnits(QPageLayout.Millimeter)
    param.setRightMargin(20.0)
    param.setLeftMargin(20.0)
    param.setTopMargin(20.0)
    param.setBottomMargin(15.0)

    loader.printToPdf("test.pdf", param)


loader.loadFinished.connect(emit_pdf)

app.exec()
