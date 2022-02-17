from PySide6.QtWidgets import QLabel

from base_widgets import BaseForm, PlainTextEditTabAction, LineEditWithTip
from models import Division


class DivisionForm(BaseForm):
    def __init__(self, person: str, division: Division = None) -> None:
        super().__init__()
        self.person = person
        self.division = division

        # input elements
        self.division_full_name_pte = PlainTextEditTabAction()
        self.division_red_name_pte = PlainTextEditTabAction()
        self.division_address_le = LineEditWithTip()
        self.division_phone_le = LineEditWithTip()

        # configuration
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.cancel_button)
        self.form_layout.addRow(QLabel('Полное наименование:'), self.division_full_name_pte)
        self.form_layout.addRow(QLabel('Сокращенное:'), self.division_red_name_pte)
        self.form_layout.addRow(QLabel('Почтовый адрес:'), self.division_address_le)
        self.form_layout.addRow(QLabel('Телефон:'), self.division_phone_le)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        self.division_full_name_pte.textChanged.connect(self.activate_button)
        self.division_red_name_pte.textChanged.connect(self.activate_button)
        self.division_address_le.textChanged.connect(self.activate_button)
        self.division_phone_le.textChanged.connect(self.activate_button)

        self.activate_button()

    def activate_button(self) -> None:
        self.add_button.setDisabled(self.field_validator())

    def field_validator(self) -> bool:
        fields = [
            True if self.division_full_name_pte.toPlainText() else False,
            True if self.division_red_name_pte.toPlainText() else False,
            True if self.division_address_le.text() else False,
            True if self.division_phone_le.text() else False
        ]
        return False in fields

    def check_for_uniqueness(self) -> Division or None:
        return Division.get_by_red_name(self.division_red_name_pte.toPlainText(), self.person)

    def add_division(self) -> Division:
        return Division(**self.get_data_from_form()).save()

    def edit_division(self) -> Division:
        self.division.division_full_name = self.division_full_name_pte.toPlainText(),
        self.division.division_red_name = self.division_red_name_pte.toPlainText(),
        self.division.division_address = self.division_address_le.text(),
        self.division.phone = self.division_phone_le.text(),
        self.division.person = self.person
        self.division.update()
        return self.division

    def get_data_from_form(self) -> dict:
        return dict(
            division_full_name=self.division_full_name_pte.toPlainText(),
            division_red_name=self.division_red_name_pte.toPlainText(),
            division_address=self.division_address_le.text(),
            phone=self.division_phone_le.text(),
            person=self.person
        )

    def set_data_in_form(self) -> None:
        self.division_full_name_pte.setPlainText(self.division.division_full_name)
        self.division_red_name_pte.setPlainText(self.division.division_red_name)
        self.division_address_le.setText(self.division.division_address)
        self.division_phone_le.setText(self.division.phone)
