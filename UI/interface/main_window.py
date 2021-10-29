import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from UI.interface.person_data_form import PersonaReferralForm
from UI.ui_py.research_main_window import Ui_research_main_window


class MainWindow(QMainWindow, Ui_research_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.person_data_form = None
        self.data = {}

        # slots
        self.add_person.clicked.connect(self.create_person)

    def create_person(self):
        self.person_data_form = PersonaReferralForm()
        event = self.person_data_form.exec()
        if event:
            self.data = self.person_data_form.get_info()
            self.load_in_table()

    def load_in_table(self):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.data['surname']))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(self.data['name']))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(self.data['middle_name']))
        self.tableWidget.setItem(row_position, 5, QTableWidgetItem(self.data['date_of_birth']))
        self.tableWidget.setItem(row_position, 6, QTableWidgetItem(self.data['birthplace']))
        if self.data['case_category'] == 'criminal':
            number = 'у/д № {}'.format(self.data['number'])
            self.tableWidget.setItem(row_position, 7, QTableWidgetItem(number))
        elif self.data['case_category'] == 'incident':
            number = 'КУСП № {}'.format(self.data['number'])
            self.tableWidget.setItem(row_position, 7, QTableWidgetItem(number))
        elif self.data['case_category'] == 'requisition':
            number = 'Требование № {}'.format(self.data['number'])
            self.tableWidget.setItem(row_position, 7, QTableWidgetItem(number))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
