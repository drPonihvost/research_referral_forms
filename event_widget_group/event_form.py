from typing import List, Dict

from PySide2.QtWidgets import QGridLayout, QRadioButton, QButtonGroup, QVBoxLayout

from base_widgets import BaseForm
from error_widget import ErrorWidget
from event_widget_group.event_case_widget import EventCaseWidget
from event_widget_group.other_event_widget import OtherCaseWidget
from models import Event


class EventForm(BaseForm):
    def __init__(self):
        super().__init__()
        self.__column = 3

        # widgets
        self.event_case_widget = None

        # layout
        self.radio_layout = QGridLayout()
        self.event_case_widget_layout = QVBoxLayout()
        self.case_button_group = QButtonGroup()

    def setup_ui(self):
        # configuration
        self.set_window_config()
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.cancel_button)
        for element in enumerate(self.create_rpb_config()):
            radio_button = QRadioButton(element[1]['layout'])
            radio_button.setObjectName(element[1]['orm'])
            self.case_button_group.addButton(radio_button)
            self.radio_layout.addWidget(radio_button, element[0] // self.__column + 1, element[0] % self.__column)
        self.main_layout.addLayout(self.radio_layout)
        self.main_layout.addLayout(self.event_case_widget_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        # signals
        self.case_button_group.buttonClicked.connect(self.set_event_case_widget)
        self.case_button_group.buttonToggled.connect(self.set_event_case_widget)

    def set_event_case_widget(self, button) -> None:
        for i in reversed(range(self.event_case_widget_layout.count())):
            self.event_case_widget_layout.itemAt(i).widget().deleteLater()
        self.event_case_widget = OtherCaseWidget()
        if button.objectName() != 'other':
            self.event_case_widget = EventCaseWidget()
        self.event_case_widget.setup_ui(button.objectName())
        self.activate_button()
        config = self.event_case_widget.create_input_config()
        for element in config:
            if element.get('signal'):
                element['signal'](self.activate_button)
        self.event_case_widget_layout.addWidget(self.event_case_widget)

    def set_radio(self, case_type: str) -> None:
        self.findChild(QRadioButton, case_type).toggle()

    def activate_button(self) -> None:
        self.add_button.setEnabled(self.event_case_widget.field_validator())

    def get_data(self) -> Dict:
        data = self.event_case_widget.get_data()
        data['case_type'] = self.case_button_group.checkedButton().objectName()
        return data

    def set_data(self, db_event: Event) -> None:
        self.set_radio(db_event.case_type)
        self.event_case_widget.set_data(db_event)

    def validate(self, **kwargs) -> List:
        error_list = []
        for element in self.event_case_widget.create_input_config():
            if element.get('validator'):
                v_data = element['validator'](element, **kwargs)
                if v_data:
                    error_list.append(v_data)
        return error_list

    def accept(self) -> Dict or None:
        error_list = self.validate(case_type=self.case_button_group.checkedButton().objectName())
        v_date = self.validate_date()
        if v_date:
            error_list.append(v_date)
        if error_list:
            error_widget = ErrorWidget(title='Ошибка валидации')
            error_widget.set_error_list(error_list=error_list)
            error_widget.exec()
            return
        super().accept()

    @staticmethod
    def create_rpb_config() -> List:
        criminal = {
            'orm': 'criminal',
            'layout': 'Уголовное дело',
            'widget': EventCaseWidget
        }
        incident = {
            'orm': 'incident',
            'layout': 'КУСП',
            'widget': EventCaseWidget
        }
        search_case = {
            'orm': 'search_case',
            'layout': 'Розыскное дело',
            'widget': EventCaseWidget
        }
        inspection_material = {
            'orm': 'inspection_material',
            'layout': 'Материалы проверки',
            'widget': EventCaseWidget
        }
        other = {
            'orm': 'other',
            'layout': 'Иное',
            'widget': OtherCaseWidget
        }
        return [criminal, incident, search_case, inspection_material, other]

    @staticmethod
    def check_for_uniqueness(data: Dict) -> Event or None:
        return Event.get_event_by_data(data['case_type'], data['number'], data['formation_date'])

    def validate_date(self) -> str or None:
        data = self.get_data()
        if data['incident_date'] > data['formation_date']:
            return f'Дата происшествия не может быть позже даты формирования материалов'
