from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem

from UI.interface.base_widgets import BaseWidget, ResearchTable
from data_base.models import Research, PersonToCheck, OfficialPerson


class ResearchWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        # layout
        self.main_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()

        # widgets
        self.table = ResearchTable()

        # buttons
        self.add_research_pb = QPushButton('Создать')
        self.change_research_pb = QPushButton('Изменить')
        self.form_research_pb = QPushButton('Сформировать')
        self.delete_research_pb = QPushButton('Удалить')

        # configuration
        self.button_layout.addWidget(self.add_research_pb)
        self.button_layout.addWidget(self.change_research_pb)
        self.button_layout.addWidget(self.form_research_pb)
        self.button_layout.addWidget(self.delete_research_pb)
        self.button_layout.addStretch(0)
        self.table_layout.addWidget(self.table)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.table_layout)
        self.setLayout(self.main_layout)

        # actions
        self.center_and_set_the_size(0.95, 0.8)
        self.table.resize_to_content()
        self.fill_the_table(Research.get_all())

    # slots
    def fill_the_table(self, researches: list[Research]):
        self.table.setRowCount(0)
        if not researches:
            return
        for research in researches:
            persons_to_check_count = PersonToCheck.get_count_by_research(research.id)
            initiator = OfficialPerson.get_name_by_research(research.id, 'initiator')
            addressee = OfficialPerson.get_name_by_research(research.id, 'addressee')
            executor = OfficialPerson.get_name_by_research(research.id, 'executor')
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(research.id)))
            self.table.setItem(row, 1, QTableWidgetItem(research.convert_recording_date()))
            self.table.setItem(row, 2, QTableWidgetItem(research.convert_change_date()))
            self.table.setItem(row, 3, QTableWidgetItem(research.event.number_to_string()))
            self.table.setItem(row, 4, QTableWidgetItem(research.event.convert_incident_date()))
            self.table.setItem(row, 5, QTableWidgetItem(research.event.address))
            self.table.setItem(row, 6, QTableWidgetItem(research.event.plot))
            self.table.setItem(row, 7, QTableWidgetItem(research.event.article))
            self.table.setItem(row, 8, QTableWidgetItem(str(persons_to_check_count)))
            self.table.setItem(row, 9, QTableWidgetItem(research.convert_dispatch_date()))
            self.table.setItem(row, 10, QTableWidgetItem(initiator))
            self.table.setItem(row, 11, QTableWidgetItem(addressee))
            self.table.setItem(row, 12, QTableWidgetItem(executor))
        self.table.resize_to_content()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = ResearchWidget()
    w.show()
    sys.exit(app.exec())
