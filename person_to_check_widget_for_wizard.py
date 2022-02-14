from PySide6.QtWidgets import QPushButton, QTableWidgetItem, QVBoxLayout, QHBoxLayout

from base_widgets import PersonTableForWizard, BaseWidget
from person_to_check_form import PersonToCheckForm
from models import PersonToCheck


class PersonToCheckWidgetForWizard(BaseWidget):
    def __init__(self, research):
        super().__init__()
        self.research = research
        # layout
        self.main_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()

        # widgets
        self.table = PersonTableForWizard()

        # buttons
        self.add_button = QPushButton('Добавить')
        self.edit_person_pb = QPushButton('Изменить')
        self.delete_person_pb = QPushButton('Удалить')

        # configuration
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.edit_person_pb)
        self.button_layout.addWidget(self.delete_person_pb)
        self.button_layout.addStretch(0)
        self.table_layout.addWidget(self.table)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.table_layout)
        self.setLayout(self.main_layout)

        # signals
        self.add_button.clicked.connect(self.add_person)
        self.add_button.clicked.connect(self.activate_button)
        self.edit_person_pb.clicked.connect(self.edit_person)
        self.edit_person_pb.clicked.connect(self.activate_button)
        self.delete_person_pb.clicked.connect(self.delete_person)
        self.delete_person_pb.clicked.connect(self.activate_button)
        self.table.itemSelectionChanged.connect(self.activate_button)

        # actions
        self.table.resize_to_content()
        self.fill_the_table(PersonToCheck.get_by_research(self.research.id))
        self.activate_button()

    # slots
    def activate_button(self):
        enabled = True if self.table.selectionModel().selectedRows(0) else False
        self.edit_person_pb.setEnabled(enabled)
        self.delete_person_pb.setEnabled(enabled)

    def fill_the_table(self, persons: list[PersonToCheck]):
        self.table.setRowCount(0)
        if not persons:
            return
        for person in reversed(persons):
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(person.surname))
            self.table.setItem(row, 1, QTableWidgetItem(person.name))
            self.table.setItem(row, 2, QTableWidgetItem(person.patronymic))
            self.table.setItem(row, 3, QTableWidgetItem(person.convert_date()))
            self.table.setItem(row, 4, QTableWidgetItem(person.get_gender()))
            self.table.setItem(row, 5, QTableWidgetItem(person.related))
            self.table.setItem(row, 6, QTableWidgetItem(person.birthplace))
            self.table.setItem(row, 7, QTableWidgetItem(person.reg_place))
            self.table.setItem(row, 8, QTableWidgetItem(str(person.id)))
        self.table.resize_to_content()

    def add_person(self):
        person_to_check_form = PersonToCheckForm(self.research)
        event = person_to_check_form.exec()
        if event:
            data = person_to_check_form.get_data()
            PersonToCheck(**data).save()
        self.fill_the_table(PersonToCheck.get_by_research(self.research.id))

    def edit_person(self):
        person_id = self.table.item(self.table.currentRow(), 8).text()
        person = PersonToCheck.get_by_id(person_id)
        person_to_check_form = PersonToCheckForm(person.research)
        person_to_check_form.fill_the_form(person)
        event = person_to_check_form.exec()
        if event:
            data = person_to_check_form.get_data()
            person.surname = data['surname']
            person.name = data['name']
            person.patronymic = data['patronymic']
            person.male = data['male']
            person.birthday = data['birthday']
            person.birthplace = data['birthplace']
            person.related = data['related']
            person.reg_place = data['reg_place']
            person.update()
        self.fill_the_table(PersonToCheck.get_by_research(self.research.id))

    def delete_person(self):
        person_id = self.table.item(self.table.currentRow(), 8).text()
        person = PersonToCheck.get_by_id(person_id)
        person.delete()
        self.fill_the_table(PersonToCheck.get_by_research(self.research.id))
