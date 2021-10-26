import json
import sys

import qrcode
from PIL.ImageQt import ImageQt


from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPixmap
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm

from UI.ui_py.persona_referal_form import Ui_persona_referal_form
from UI.ui_py.ud_form import Ui_ud_form
from UI.ui_py.kusp_form import Ui_kusp_form
from UI.ui_py.req_form import Ui_Form


class UdForm(QWidget, Ui_ud_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_info(self):
        number = self.number_cb.text()
        formation_date = self.formation_date_le.text()
        item = self.item_de.currentText()
        address = self.number_cb_2.text()
        return number, formation_date, item, address



class KUSPForm(QWidget, Ui_kusp_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class ReqForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class PersonaReferalForm(QWidget, Ui_persona_referal_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_event_type()

        # signals
        self.ud_rb.toggled.connect(self.set_event_type)
        self.kusp_rb.toggled.connect(self.set_event_type)
        self.req_rb.toggled.connect(self.set_event_type)
        self.save_btn.clicked.connect(print(self.form.get_info()))

    def set_event_type(self):
        for i in reversed(range(self.event_lo.count())):
            self.event_lo.itemAt(i).widget().deleteLater()
        if self.ud_rb.isChecked():
            self.form = UdForm()
        elif self.kusp_rb.isChecked():
            self.form = KUSPForm()
        elif self.req_rb.isChecked():
            self.form = ReqForm()
        self.event_lo.addWidget(self.form)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = PersonaReferalForm()
    w.show()
    sys.exit(app.exec())