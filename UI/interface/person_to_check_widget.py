from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem

from UI.interface.base_widgets import PersonTable, BaseWidget
from data_base.models import Research, PersonToCheck, OfficialPerson


class PersonToCheckWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        # layout
        self.main_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()

        # widgets
        self.table = PersonTable()

        # buttons
        self.change_person_pb = QPushButton('Изменить')
        self.delete_person_pb = QPushButton('Удалить')

        # configuration
        self.button_layout.addWidget(self.change_person_pb)
        self.button_layout.addWidget(self.delete_person_pb)
        self.button_layout.addStretch(0)
        self.table_layout.addWidget(self.table)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.table_layout)
        self.setLayout(self.main_layout)

        # actions
        self.center_and_set_the_size(0.95, 0.8)
        self.table.resize_to_content()
        self.fill_the_table(PersonToCheck.get_all())

        # slots

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
            self.table.setItem(row, 4, QTableWidgetItem(person.birthplace))
            self.table.setItem(row, 5, QTableWidgetItem(person.get_gender()))
            self.table.setItem(row, 6, QTableWidgetItem(person.research.event.number_to_string()))
            self.table.setItem(row, 7, QTableWidgetItem(person.research.convert_dispatch_date()))
        self.table.resize_to_content()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = PersonToCheckWidget()
    w.show()
    sys.exit(app.exec())