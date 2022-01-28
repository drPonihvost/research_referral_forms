from PySide6.QtWidgets import QLabel

from base_widgets import BaseForm, PlainTextEditTabAction


class DivisionForm(BaseForm):
    def __init__(self):
        super().__init__()

        # input elements
        self.division_full_name = PlainTextEditTabAction()
        self.division_red_name = PlainTextEditTabAction()

        # configuration
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.cancel_button)
        self.form_layout.addRow(QLabel('Полное наименование:'), self.division_full_name)
        self.form_layout.addRow(QLabel('Сокращенное:'), self.division_red_name)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)
