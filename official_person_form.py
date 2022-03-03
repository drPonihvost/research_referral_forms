from PySide2.QtWidgets import QHBoxLayout, QComboBox, QPushButton, QLabel

from base_widgets import BaseForm, LineEditWithTip
from division_form import DivisionForm
from error_widget import ErrorWidget
from models import Division, Initiator, Addressee, Executor


class OfficialPersonForm(BaseForm):
    def __init__(self, person: str = 'initiator'):
        super().__init__()
        self.set_window_config()

        self.persons = dict(
            initiator=Initiator,
            addressee=Addressee,
            executor=Executor
        )

        self.person = person

        nominative_case = dict(
            surname_tip='Иванов',
            name_tip='Иван',
            patronymic_tip='Иванович',
            rank_tip='капитан полиции',
            post_tip='начальник'
        )

        dative_case = dict(
            surname_tip='Иванову',
            name_tip='Ивану',
            patronymic_tip='Ивановичу',
            rank_tip='капитану полиции',
            post_tip='начальнику'
        )

        tip_text = nominative_case

        if self.person == 'addressee':
            tip_text = dative_case

        # layouts
        self.division_button_layout = QHBoxLayout()

        # input elements
        self.surname_le = LineEditWithTip(tip=tip_text['surname_tip'])
        self.name_le = LineEditWithTip(tip=tip_text['name_tip'])
        self.patronymic_le = LineEditWithTip(tip=tip_text['patronymic_tip'])
        self.post_le = LineEditWithTip(tip=tip_text['post_tip'])
        self.division_cb = QComboBox()
        self.division_cb.setMaximumWidth(self.width()*0.6)
        self.rank_le = LineEditWithTip(tip=tip_text['rank_tip'])

        # button elements
        self.add_division_button = QPushButton('Добавить')
        self.edit_division_button = QPushButton('Редактировать')
        self.delete_division_button = QPushButton('Удалить')

        # configuration
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.cancel_button)
        self.form_layout.addRow(QLabel('Подразделение:'), self.division_cb)
        self.form_layout.addRow(QLabel(), self.division_button_layout)
        self.division_button_layout.addWidget(self.add_division_button)
        self.division_button_layout.addWidget(self.edit_division_button)
        self.division_button_layout.addWidget(self.delete_division_button)
        self.form_layout.addRow(QLabel('Фамилия:'), self.surname_le)
        self.form_layout.addRow(QLabel('Имя:'), self.name_le)
        self.form_layout.addRow(QLabel('Отчество:'), self.patronymic_le)
        self.form_layout.addRow(QLabel('Спец. звание:'), self.rank_le)
        self.form_layout.addRow(QLabel('Должность'), self.post_le)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        # signal
        self.add_division_button.clicked.connect(self.add_division)
        self.add_division_button.clicked.connect(self.activate_button)
        self.edit_division_button.clicked.connect(self.edit_division)
        self.edit_division_button.clicked.connect(self.activate_button)
        self.delete_division_button.clicked.connect(self.delete_division)
        self.delete_division_button.clicked.connect(self.activate_button)
        self.division_cb.activated.connect(self.activate_button)
        self.surname_le.textChanged.connect(self.activate_button)
        self.name_le.textChanged.connect(self.activate_button)
        self.patronymic_le.textChanged.connect(self.activate_button)
        self.post_le.textChanged.connect(self.activate_button)
        self.rank_le.textChanged.connect(self.activate_button)

        # action
        self.fill_combo_box()
        self.division = self.get_division()
        self.activate_button()

    # slots
    def activate_button(self):
        enable = True if self.division_cb.currentText() else False
        self.edit_division_button.setEnabled(enable)
        self.delete_division_button.setEnabled(enable)
        self.add_button.setEnabled(enable and not self.field_validator())

    def field_validator(self) -> bool:
        fields = [
            True if self.surname_le.text() else False,
            True if self.name_le.text() else False,
            True if self.patronymic_le.text() else False,
            True if self.post_le.text() else False,
            True if self.rank_le.text() else False
        ]
        return False in fields

    def fill_combo_box(self):
        self.division_cb.clear()
        divisions = Division.get_by_person(self.person)
        if not divisions:
            return
        for division in divisions:
            self.division_cb.addItem(division.division_red_name)

    def fill_the_form(self, official_person):
        self.surname_le.setText(official_person.surname)
        self.name_le.setText(official_person.name)
        self.patronymic_le.setText(official_person.patronymic)
        self.post_le.setText(official_person.post)
        self.division_cb.setCurrentText(official_person.division.division_red_name)
        self.rank_le.setText(official_person.rank)

    def get_division(self):
        division = Division.get_by_red_name(
            self.division_cb.currentText(),
            self.person
        )
        return division

    def get_data(self):
        division = self.get_division()
        if not division:
            message = ErrorWidget(
                text='Отсутствует подразделение',
                title='Ошибка валидации'
            )
            message.exec()
            return
        return dict(
            division=division,
            surname=self.surname_le.text(),
            name=self.name_le.text(),
            patronymic=self.patronymic_le.text(),
            rank=self.rank_le.text(),
            post=self.post_le.text()
        )

    def add_division(self):
        division_form_dialog = DivisionForm(division=self.get_division(), person=self.person)
        event = division_form_dialog.exec()
        if event:
            division = division_form_dialog.check_for_uniqueness()
            if not division:
                division_form_dialog.add_division()
            else:
                message = ErrorWidget(
                    text='Такая запись уже существует',
                    title='Ошибка добавления'
                )
                message.exec()
        self.fill_combo_box()

    def edit_division(self):
        division_form_dialog = DivisionForm(division=self.get_division(), person=self.person)
        division_form_dialog.set_data_in_form()
        event = division_form_dialog.exec()
        if event:
            division = division_form_dialog.check_for_uniqueness()
            if not division:
                division_form_dialog.edit_division()
            else:
                message = ErrorWidget(
                    text='Такая запись уже существует',
                    title='Ошибка редактирования'
                )
                message.exec()
        self.fill_combo_box()

    def delete_division(self):
        division = Division.get_by_red_name(self.division_cb.currentText(), self.person)
        person = self.persons[self.person].get_by_division(division.id)
        if not person:
            division.delete()
        else:
            message = ErrorWidget(
                text='''Подразделение не может быть удалено''',
                title='Ошибка удаления'
            )
            message.exec()
        self.fill_combo_box()
