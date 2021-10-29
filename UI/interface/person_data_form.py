from PySide6.QtWidgets import QDialog, QWidget

from UI.ui_py.kusp_form import Ui_kusp_form
from UI.ui_py.persona_referal_form import Ui_persona_referal_form
from UI.ui_py.req_form import Ui_Form
from UI.ui_py.ud_form import Ui_ud_form


class CriminalCaseForm(QWidget, Ui_ud_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_info_in_form(self):
        return {
            'case_category': 'criminal',
            'number': self.number_cb.text(),
            'formation_date': self.formation_date_le.text(),
            'item': self.item_de.currentText(),
            'address': self.number_cb_2.text()
        }


class IncidentForm(QWidget, Ui_kusp_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_info_in_form(self):
        return {
            'case_category': 'incident',
            'number': self.number_cb.text(),
            'formation_date': self.formation_date_le.text(),
            'item': self.item_de.currentText(),
            'address': self.number_cb_2.text()
        }


class RequisitionForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_info_in_form(self):
        return {
            'case_category': 'requisition',
            'number': self.number_cb.text(),
            'formation_date': self.formation_date_le.text(),
        }


class PersonaReferralForm(QDialog, Ui_persona_referal_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.event_description_form = None
        self.set_event_type()

        # signals
        self.ud_rb.toggled.connect(self.set_event_type)
        self.kusp_rb.toggled.connect(self.set_event_type)
        self.req_rb.toggled.connect(self.set_event_type)
        self.save_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

    def get_info(self):

        data = self.event_description_form.get_info_in_form()
        male = 'male' if self.male_rb.isChecked() else 'female'
        info = {
            'surname': self.surname_le.text(),
            'name': self.name_le.text(),
            'middle_name': self.middle_name_le.text(),
            'male': male,
            'date_of_birth': self.date_of_birth_de.text(),
            'birthplace': self.birthplace_le.text(),
            'plot': self.plot_te.toPlainText()
        }
        info.update(data)
        # self.surname_le.clear()
        # self.name_le.clear()
        # self.middle_name_le.clear()
        # self.date_of_birth_de.clear()
        # self.birthplace_le.clear()
        # self.plot_te.clear()
        return info

    def set_event_type(self):
        for i in reversed(range(self.event_lo.count())):
            self.event_lo.itemAt(i).widget().deleteLater()
        if self.ud_rb.isChecked():
            self.event_description_form = CriminalCaseForm()
        elif self.kusp_rb.isChecked():
            self.event_description_form = IncidentForm()
        elif self.req_rb.isChecked():
            self.event_description_form = RequisitionForm()
        self.event_lo.addWidget(self.event_description_form)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = PersonaReferralForm()
#     w.show()
#     sys.exit(app.exec())
