import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow

from UI.interface.main_official_person_data_widget import OfficialPersonData
from UI.interface.person_data_form import PersonaReferralForm
from UI.ui_py.research_main_window import Ui_research_main_window
from data_base.models import Research, PersonToCheck, Criminal, Incident, SearchCase, InspectionMaterial, Requisition, \
    Event


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
            self.add_person.setDisabled(True)

    # def form_research_table(self):
    #     data = ResearchDBModel.get_all()
    #     for i in data:
    #         row_position = self.research_person_table_tw.rowCount()
    #         self.research_person_table_tw.insertRow(row_position)
    #         self.research_person_table_tw.setItem(row_position, 0, QTableWidgetItem(i.id))
    #         self.research_person_table_tw.setItem(row_position, 1, QTableWidgetItem(i.date_of_recording))
    #         person = PersonToCheckDBModel.get_by_id(i.person_id)
    #         self.research_person_table_tw.setItem(row_position, 2, QTableWidgetItem(person.surname))
    #         self.research_person_table_tw.setItem(row_position, 3, QTableWidgetItem(person.name))
    #         self.research_person_table_tw.setItem(row_position, 4, QTableWidgetItem(person.middle_name))
    #         self.research_person_table_tw.setItem(row_position, 5, QTableWidgetItem(person.date_of_birth))
    #         self.research_person_table_tw.setItem(row_position, 6, QTableWidgetItem(self.data['birthplace']))

    def create_person(self):
        self.person_data_form = PersonaReferralForm()
        event = self.person_data_form.exec()
        if event:
            self.data = self.person_data_form.get_info()
            self.load_research()

    def load_research(self):
        addressees_id = self.official_person_data_addresses.official_person_id
        executor_id = self.official_person_data_executor.official_person_id
        initiator_id = self.official_person_data_initiator.official_person_id

        research = Research(
            initiator_id=initiator_id,
            executor_id=executor_id,
            addressees_id=addressees_id
        )
        person = PersonToCheck(
            surname=self.data['surname'],
            name=self.data['name'],
            middle_name=self.data['middle_name'],
            birthday=self.data['date_of_birth'],
            birthplace=self.data['birthplace'],
            male=self.data['male']
        )
        event_data = dict(
            number=self.data['number'],
            formation_date=self.data['formation_date'],
            plot=self.data['plot']
        )
        if self.data['case_category'] != 'requisition':
            event_data.update(
                address=self.data['address'],
                article=self.data['item'],
            )
        event = Event(
            case_type=self.data['case_category']
        )
        if self.data['case_category'] == 'criminal':
            event.criminal = Criminal(
                **event_data
            )
        elif self.data['case_category'] == 'incident':
            event.incident = Incident(
                **event_data
            )
        elif self.data['case_category'] == 'search_case':
            event.search_case = SearchCase(
                **event_data
            )
        elif self.data['case_category'] == 'inspection_material':
            event.inspection_material = InspectionMaterial(
                **event_data
            )
        elif self.data['case_category'] == 'requisition':
            event.requisition = Requisition(
                **event_data
            )
        research.person = person
        research.event = event
        research.save()

        # person = PersonToCheck(
        #     surname=self.data['surname'],
        #     name=self.data['name'],
        #     middle_name=self.data['middle_name'],
        #     birthday=self.data['date_of_birth'],
        #     birthplace=self.data['birthplace'],
        #     male=self.data['male']
        # )
        # event_type = dict(
        #     criminal=Criminal,
        #     incident=Incident,
        #     search_case=SearchCase,
        #     inspection_material=InspectionMaterial
        # )
        # event_data = dict(
        #     number=self.data['number'],
        #     formation_date=self.data['formation_date'],
        # )
        # if self.data['case_category'] != 'requisition':
        #     event_data.update(
        #         incident=self.data['item'],
        #         address=self.data['address'],
        #         article=self.data['number'],
        #     )
        # case = event_type[self.data['case_category']]
        #
        # event = {
        #     'case_type':self.data['case_category'],
        #     self.data['case_category']: case(**event_data)
        # }
        # research = Research(
        #     date_of_recording=datetime.today(),
        #     person=person,
        #     initiator=Initiator.get_by_id(initiator_id),
        #     executor=Executor.get_by_id(executor_id),
        #     addressees=Addressees.get_by_id(addressees_id),
        #     event=event
        # )
        # research.save()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
