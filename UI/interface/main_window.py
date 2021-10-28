import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


from UI.interface.person_data_form import PersonaReferralForm
from UI.ui_py.research_main_window import Ui_research_main_window


class MainWindow(QMainWindow, Ui_research_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.person_data_form = PersonaReferralForm()

        # slots
        self.add_person.clicked.connect(self.create_person)

    def create_person(self):
        self.person_data_form.show()
        self.person_data_form.save_btn.clicked.connect(self.load_in_table)
        self.person_data_form.info = {}

    def load_in_table(self):
        row_position = self.tableWidget.rowCount()
        print('Позиция' + str(row_position))
        self.tableWidget.insertRow(row_position)
        print('Значение' + self.person_data_form.info['surname'])
        value = self.person_data_form.info['surname']
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(value))

        # if self.person_data_form.info:
        #     if self.person_data_form.info['action'] == 'cancel':
        #         print('Отмена')
        #         self.person_data_form.info = {}
        #         return
        # else:
        #     row_position = self.tableWidget.rowCount()
        #     print('Позиция' + str(row_position))
        #     self.tableWidget.insertRow(row_position)
        #     print('Значение' + self.person_data_form.info['surname'])
        #     self.tableWidget.setItem(row_position, 0, self.person_data_form.info['surname'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
