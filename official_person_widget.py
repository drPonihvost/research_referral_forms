from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem

from base_widgets import BaseWidget, OfficialPersonTable
from official_person_form import OfficialPersonForm
from models import Initiator, Executor, Addressee


class OfficialPersonWidget(BaseWidget):
    def __init__(self, person):
        super().__init__()
        _TABLE = dict(
            initiator=Initiator,
            executor=Executor,
            addressee=Addressee
        )

        self.person = person
        self.base_class = _TABLE[self.person]
        self.table = OfficialPersonTable(self.person)

        # layout
        self.main_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()
        self.button_layout = QVBoxLayout()

        # button elements
        self.add_button = QPushButton('Добавить')
        self.edit_button = QPushButton('Изменить')
        self.delete_button = QPushButton('Удалить')

        # signal
        self.add_button.clicked.connect(self.add_official_person)
        self.edit_button.clicked.connect(self.edit_official_person)
        self.delete_button.clicked.connect(self.delete_official_person)
        self.table.itemSelectionChanged.connect(self.activate_button)

        # configuration
        self.table_layout.addWidget(self.table)
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.edit_button)
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addStretch(1)
        self.main_layout.addLayout(self.table_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        # actions
        self.fill_the_table()
        self.activate_button()

    # slots
    def fill_the_table(self):
        self.table.setRowCount(0)
        official_persons = self.base_class.get_all()
        if not official_persons:
            return
        for official_person in reversed(official_persons):
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(official_person.create_name_reduction()))
            self.table.setItem(row, 1, QTableWidgetItem(official_person.division.division_red_name))
            self.table.setItem(row, 2, QTableWidgetItem(official_person.post.capitalize()))
            self.table.setItem(row, 3, QTableWidgetItem(official_person.rank.lower()))
            self.table.setItem(row, 4, QTableWidgetItem(official_person.division.division_full_name))
            self.table.setItem(row, 5, QTableWidgetItem(str(official_person.id)))
        self.table.resize_to_content()

    def activate_button(self):
        enabled = True if self.table.selectionModel().selectedRows(0) else False
        self.edit_button.setEnabled(enabled)
        self.delete_button.setEnabled(enabled)

    def add_official_person(self):
        official_person_form = OfficialPersonForm(self.person)
        event = official_person_form.exec()
        if event:
            data = official_person_form.get_data()
            self.base_class(
                **data
            ).save()
        self.fill_the_table()
        self.activate_button()

    def edit_official_person(self):
        official_person = self.table.selectedItems()[5].text()
        official_person = self.base_class.get_by_id(official_person)
        official_person_form = OfficialPersonForm(self.person)
        official_person_form.fill_the_form(official_person)
        event = official_person_form.exec()
        if event:
            data = official_person_form.get_data()
            official_person.division = data['division']
            official_person.surname = data['surname']
            official_person.name = data['name']
            official_person.patronymic = data['patronymic']
            official_person.rank = data['rank']
            official_person.post = data['post']
            official_person.update()
        self.fill_the_table()
        self.activate_button()

    def delete_official_person(self):
        official_person = self.base_class.get_by_id(self.table.selectedItems()[5].text())
        official_person.delete()
        self.fill_the_table()
        self.activate_button()
