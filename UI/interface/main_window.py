import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from UI.interface.main_official_person_data_widget import OfficialPersonData
from UI.interface.person_data_form import PersonaReferralForm
from UI.ui_py.research_main_window import Ui_research_main_window
from data_base.models import ResearchDBModel,  PersonToCheckDBModel


class MainWindow(QMainWindow, Ui_research_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.person_data_form = None
        self.data = {}
        self.official_person_data_initiator = OfficialPersonData(role='initiator')
        self.initiator_lo.addWidget(self.official_person_data_initiator)
        self.official_person_data_addresses = OfficialPersonData(role='addressees')
        self.addressee_lo.addWidget(self.official_person_data_addresses)
        self.official_person_data_executor = OfficialPersonData(role='executor')
        self.executor_lo.addWidget(self.official_person_data_executor)
        self.verify_official_person()

        # slots
        self.add_person.clicked.connect(self.create_person)
        self.official_person_data_executor.choice_pb.clicked.connect(self.verify_official_person)
        self.official_person_data_addresses.choice_pb.clicked.connect(self.verify_official_person)
        self.official_person_data_initiator.choice_pb.clicked.connect(self.verify_official_person)

    def verify_official_person(self):
        if self.official_person_data_initiator.name_le.text() and \
                self.official_person_data_executor.name_le.text() and \
                self.official_person_data_addresses.name_le.text():
            self.add_person.setEnabled(True)
        else:
            self.add_person.setEnabled(True)

    def form_research_table(self):
        data = ResearchDBModel.get_all()
        for i in data:
            row_position = self.research_person_table_tw.rowCount()
            self.research_person_table_tw.insertRow(row_position)
            self.research_person_table_tw.setItem(row_position, 0, QTableWidgetItem(i.id))
            self.research_person_table_tw.setItem(row_position, 1, QTableWidgetItem(i.date_of_recording))
            person = PersonToCheckDBModel.get_by_id(i.person_id)
            self.research_person_table_tw.setItem(row_position, 2, QTableWidgetItem(person.surname))
            self.research_person_table_tw.setItem(row_position, 3, QTableWidgetItem(person.name))
            self.research_person_table_tw.setItem(row_position, 4, QTableWidgetItem(person.middle_name))
            self.research_person_table_tw.setItem(row_position, 5, QTableWidgetItem(person.date_of_birth))
            self.research_person_table_tw.setItem(row_position, 6, QTableWidgetItem(self.data['birthplace']))

    def create_person(self):
        self.person_data_form = PersonaReferralForm()
        event = self.person_data_form.exec()
        if event:
            self.data = self.person_data_form.get_info()
            self.load_research()

    def load_research(self):

        row_position = self.research_person_table_tw.rowCount()
        self.research_person_table_tw.insertRow(row_position)

        self.research_person_table_tw.setItem(row_position, 2, QTableWidgetItem(self.data['surname']))
        self.research_person_table_tw.setItem(row_position, 3, QTableWidgetItem(self.data['name']))
        self.research_person_table_tw.setItem(row_position, 4, QTableWidgetItem(self.data['middle_name']))
        self.research_person_table_tw.setItem(row_position, 5, QTableWidgetItem(self.data['date_of_birth']))
        self.research_person_table_tw.setItem(row_position, 6, QTableWidgetItem(self.data['birthplace']))
        if self.data['case_category'] == 'criminal':
            number = 'у/д № {}'.format(self.data['number'])
            self.research_person_table_tw.setItem(row_position, 7, QTableWidgetItem(number))
        elif self.data['case_category'] == 'incident':
            number = 'КУСП № {}'.format(self.data['number'])
            self.research_person_table_tw.setItem(row_position, 7, QTableWidgetItem(number))
        elif self.data['case_category'] == 'requisition':
            number = 'Требование № {}'.format(self.data['number'])
            self.research_person_table_tw.setItem(row_position, 7, QTableWidgetItem(number))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
