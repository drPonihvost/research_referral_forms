import datetime
from typing import Dict, List

from PySide2.QtWidgets import QLabel, QFormLayout

from base_widgets import LineEditWithTip, BaseWidget, DateLineEdit
from models import Event


class OtherCaseWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self._article = 'Статья отсутствует'
        self._tip = 'Приказ МВД по РХ № 553'

        # layout
        self.form_layout = QFormLayout()

        # input elements
        self.number_le = LineEditWithTip(tip=self._tip)
        self.formation_date_le = DateLineEdit()

    def setup_ui(self, case_type: str) -> None:
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
            'label': 'Документ:',
            'get': self.number_le.text,
            'set': self.number_le.setText,
            'signal': self.number_le.textChanged.connect
        }
        formation_date = {
            'orm': 'formation_date',
            'widget': self.formation_date_le,
            'label': 'От:',
            'get': self.formation_date_le.get_date,
            'set': self.formation_date_le.set_date,
            'validator': self.date_validator,
            'signal': self.formation_date_le.textChanged.connect
        }
        return [number, formation_date]

    def get_data(self) -> Dict:
        data = dict()
        for element in self.create_input_config():
            data[element['orm']] = element['get']()
        data['article'] = self._article
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


if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = OtherCaseWidget()
    w.setup_ui('other')
    w.set_data(Event.get_by_id(1))
    w.show()
    sys.exit(app.exec())