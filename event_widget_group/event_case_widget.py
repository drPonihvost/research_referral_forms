import datetime
from typing import Dict, List

from PySide6.QtWidgets import QLabel, QFormLayout

from base_widgets import LineEditWithTip, PlainTextEditTabAction, BaseWidget, DateLineEdit, \
    LineEditForCriminalCase, ArticleCombo
from models import Event


class EventCaseWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        # layout
        self.form_layout = QFormLayout()

        # input elements
        self.number_le = LineEditForCriminalCase()
        self.formation_date_le = DateLineEdit()
        self.article_cb = ArticleCombo()
        self.plot_te = PlainTextEditTabAction()
        self.incident_date_le = DateLineEdit()
        self.address_le = LineEditWithTip()

    def setup_ui(self, case_type: str) -> None:
        if case_type == 'criminal':
            self.number_le = LineEditForCriminalCase()
        else:
            self.number_le = LineEditWithTip()
        self.setLayout(self.form_layout)
        for element in self.create_input_config():
            self.form_layout.addRow(QLabel(element['label']), element['widget'])

    def field_validator(self) -> bool:
        for element in self.create_input_config():
            if not element['get']():
                return False
        return True

    def create_input_config(self) -> List:
        number = {
            'orm': 'number',
            'widget': self.number_le,
            'label': 'Номер материала:',
            'get': self.number_le.text,
            'set': self.number_le.setText,
            'validator': self.number_validator,
            'signal': self.number_le.textChanged.connect
        }
        formation_date = {
            'orm': 'formation_date',
            'widget': self.formation_date_le,
            'label': 'Дата формирования:',
            'get': self.formation_date_le.get_date,
            'set': self.formation_date_le.set_date,
            'validator': self.date_validator,
            'signal': self.formation_date_le.textChanged.connect
        }
        article = {
            'orm': 'article',
            'widget': self.article_cb,
            'label': 'Статья УК РФ:',
            'get': self.article_cb.currentText,
            'set': self.article_cb.setCurrentText
        }
        plot = {
            'orm': 'plot',
            'widget': self.plot_te,
            'label': 'Обстоятельства:',
            'get': self.plot_te.toPlainText,
            'set': self.plot_te.setPlainText,
            'signal': self.plot_te.textChanged.connect
        }
        incident_date = {
            'orm': 'incident_date',
            'widget': self.incident_date_le,
            'label': 'Дата происшествия:',
            'get': self.incident_date_le.get_date,
            'set': self.incident_date_le.set_date,
            'validator': self.date_validator,
            'signal': self.incident_date_le.textChanged.connect
        }
        address = {
            'orm': 'address',
            'widget': self.address_le,
            'label': 'Адрес происшествия:',
            'get': self.address_le.text,
            'set': self.address_le.setText,
            'signal': self.address_le.textChanged.connect
        }
        return [number, formation_date, article, plot, incident_date, address]

    def get_data(self) -> Dict:
        data = dict()
        for element in self.create_input_config():
            data[element['orm']] = element['get']()
        return data

    def set_data(self, db_event: Event) -> None:
        data = db_event.__dict__
        for element in self.create_input_config():
            element['set'](data[element['orm']])

    @staticmethod
    def date_validator(element, **kwargs) -> str or None:
        if not element['get']():
            return f'{element["label"]} не верный формат даты'
        if element['get']() > datetime.datetime.now():
            return f'{element["label"]} не корректна'

    @staticmethod
    def number_validator(element, **kwargs) -> str or None:
        if kwargs['case_type'] == 'criminal' and len(element['get']()) != 17:
            return f'{element["label"]} должен содержать 17 цифр'
        elif not element['get']().isnumeric() and kwargs['case_type'] != 'inspection_material':
            return f'{element["label"]} должен содержать только цифры'


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = EventCaseWidget()
    w.setup_ui('criminal')
    w.get_data()
    w.show()
    sys.exit(app.exec())

