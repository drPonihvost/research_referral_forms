from typing import List

from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem

from base_widgets import PersonTable, BaseWidget
from models import PersonToCheck
from research_wizard import ResearchWizard


class PersonToCheckWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.set_window_config()
        # layout
        self.main_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()

        # widgets
        self.table = PersonTable()

        # buttons
        self.go_over_research_pb = QPushButton('Перейти к направлению')

        # configuration
        self.button_layout.addWidget(self.go_over_research_pb)
        self.button_layout.addStretch(0)
        self.table_layout.addWidget(self.table)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.table_layout)
        self.setLayout(self.main_layout)

        # signals
        self.go_over_research_pb.clicked.connect(self.go_over_research)
        self.go_over_research_pb.clicked.connect(self.activate_button)
        self.table.itemSelectionChanged.connect(self.activate_button)

        # actions
        self.table.resize_to_content()
        self.fill_the_table(PersonToCheck.get_all())
        self.activate_button()

    def activate_button(self):
        enabled = True if self.table.selectionModel().selectedRows(0) else False
        self.go_over_research_pb.setEnabled(enabled)

    def fill_the_table(self, persons: List[PersonToCheck]):
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
            self.table.setItem(row, 5, QTableWidgetItem(person.birthplace))
            self.table.setItem(row, 6, QTableWidgetItem(person.reg_place))
            self.table.setItem(row, 7, QTableWidgetItem(str(person.id)))
            self.table.setItem(row, 8, QTableWidgetItem(person.research.event.number_to_string()))
            self.table.setItem(row, 9, QTableWidgetItem(person.research.convert_dispatch_date()))
        self.table.resize_to_content()

    def go_over_research(self):
        person = PersonToCheck.get_by_id(self.table.item(self.table.currentRow(), 7).text())
        research = person.research
        wizard = ResearchWizard(research)
        wizard.next()
        wizard.next()
        event = wizard.exec()
        if event:
            research.initiator_id = None
            research.addressee_id = None
            research.executor_id = None
            research.date_of_dispatch = None
            research.update()
        self.fill_the_table(PersonToCheck.get_all())
