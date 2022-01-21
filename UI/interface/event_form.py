from datetime import datetime

from PySide6.QtWidgets import QGridLayout, QRadioButton, QComboBox, QLabel, QButtonGroup, QAbstractButton

from UI.interface.base_widgets import BaseForm, LineEditWithTip, CASE, PlainTextEditTabAction
from data_base.models import Event


class EventForm(BaseForm):
    def __init__(self):
        super().__init__()
        __CASE_TYPE = dict(criminal='Уголовное дело', incident='КУСП', search_case='Розыскное дело',
                           inspection_material='Материалы проверки', other='Иное')
        __column = 3

        self.case = None

        # layout
        self.radio_layout = QGridLayout()
        self.case_button_group = QButtonGroup()

        # input elements
        self.number_le = LineEditWithTip()
        self.formation_date_le = LineEditWithTip()
        self.formation_date_le.setInputMask("00.00.0000")
        self.formation_date_le.setMaximumWidth(100)
        self.article_cb = QComboBox()
        self.article_cb.setMaximumWidth(350)
        self.article_cb.addItems(CASE)
        self.plot_te = PlainTextEditTabAction()
        self.incident_date_le = LineEditWithTip()
        self.incident_date_le.setInputMask("00.00.0000")
        self.incident_date_le.setMaximumWidth(100)
        self.address_le = LineEditWithTip()

        # configuration
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.cancel_button)

        for step, value in enumerate(__CASE_TYPE.items()):
            radio_button = QRadioButton(value[1])
            radio_button.setObjectName(value[0])
            self.case_button_group.addButton(radio_button)
            self.radio_layout.addWidget(radio_button, step // __column+1, step % __column)
        self.form_layout.addRow(QLabel('Категория:'), self.radio_layout)
        self.form_layout.addRow(QLabel('Номер материала:'), self.number_le)
        self.form_layout.addRow(QLabel('Дата формирования:'), self.formation_date_le)
        self.form_layout.addRow(QLabel('Статья УК РФ:'), self.article_cb)
        self.form_layout.addRow(QLabel('Обстоятельства:'), self.plot_te)
        self.form_layout.addRow(QLabel('Дата происшествия:'), self.incident_date_le)
        self.form_layout.addRow(QLabel('Адрес происшествия:'), self.address_le)

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        # signal
        self.case_button_group.buttonClicked.connect(self.select_radio)

    # slots
    @staticmethod
    def convert_date(date: str):
        f = '%d.%m.%Y'
        return datetime.strptime(date, f)

    def fill_the_form(self, event: Event):
        self.case = event.case_type
        radio = self.findChild(QRadioButton, event.case_type)
        radio.setChecked(True)
        self.number_le.setText(event.number)
        self.formation_date_le.setText(event.convert_formation_date())
        self.article_cb.setCurrentText(event.article)
        self.plot_te.setPlainText(event.plot)
        self.incident_date_le.setText(event.convert_incident_date())
        self.address_le.setText(event.address)


    def clear_form(self):
        self.number_le.clear()
        self.formation_date_le.clear()
        self.plot_te.clear()
        self.incident_date_le.clear()
        self.incident_date_le.clear()
        self.address_le.clear()

    def disable_fields(self):
        self.plot_te.setDisabled(True)
        self.incident_date_le.setDisabled(True)
        self.incident_date_le.setDisabled(True)
        self.address_le.setDisabled(True)

    def enable_fields(self):
        self.plot_te.setDisabled(False)
        self.incident_date_le.setDisabled(False)
        self.incident_date_le.setDisabled(False)
        self.address_le.setDisabled(False)

    def other_case_autofill(self):
        self.clear_form()
        self.number_le.setText('Приказ МВД по РХ № 552')
        self.formation_date_le.setText('13.09.2021')
        self.article_cb.setCurrentText('Статья отсутствует')
        self.disable_fields()

    def select_radio(self, button):
        case = button.objectName()
        self.case = case
        if case == 'other':
            self.other_case_autofill()
        else:
            self.clear_form()
            self.enable_fields()

    def get_data(self):
        data = dict(
            case_type=self.case,
            number=self.number_le.text(),
            formation_date=self.convert_date(self.formation_date_le.text()),
            article=self.article_cb.currentText(),
            incident_date=None,
            address=None,
            plot=None
        )
        if self.case != 'other':
            data['incident_date'] = self.convert_date(self.incident_date_le.text())
            data['address'] = self.address_le.text()
            data['plot'] = self.plot_te.toPlainText()
        return data


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = EventForm()
    w.show()
    sys.exit(app.exec())
