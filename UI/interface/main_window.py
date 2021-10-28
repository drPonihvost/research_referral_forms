import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


from UI.interface.person_data_form import PersonaReferralForm
from UI.ui_py.research_main_window import Ui_research_main_window


class MainWindow(QMainWindow, Ui_research_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


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
        value = self.data['surname']
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
