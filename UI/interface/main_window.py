import json
import sys

import qrcode
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage

from UI.interface.main_official_person_data_widget import OfficialPersonData
from UI.interface.person_data_form import PersonaReferralForm
from UI.ui_py.research_main_window import Ui_research_main_window
from data_base.models import Research, PersonToCheck, Criminal, Incident, SearchCase, InspectionMaterial, Requisition, \
    Event


class ResearchWindow(QMainWindow, Ui_research_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.research_person_table_tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.person_data_form = None
        self.data = {}
        self.official_person_data_initiator = OfficialPersonData(role='initiator')
        self.initiator_lo.addWidget(self.official_person_data_initiator)
        self.official_person_data_addresses = OfficialPersonData(role='addressees')
        self.addressee_lo.addWidget(self.official_person_data_addresses)
        self.official_person_data_executor = OfficialPersonData(role='executor')
        self.executor_lo.addWidget(self.official_person_data_executor)
        self.verify_official_person()
        self.form_research_table()

        # signals
        self.add_person.clicked.connect(self.create_person)
        self.official_person_data_executor.choice_pb.clicked.connect(self.verify_official_person)
        self.official_person_data_addresses.choice_pb.clicked.connect(self.verify_official_person)
        self.official_person_data_initiator.choice_pb.clicked.connect(self.verify_official_person)
        self.form_pb.clicked.connect(self.create_research_blanks)

    def form_research_table(self):
        self.research_person_table_tw.setRowCount(0)
        data = Research.get_all()
        for i in data:
            row_position = self.research_person_table_tw.rowCount()
            self.research_person_table_tw.insertRow(row_position)
            self.research_person_table_tw.setItem(row_position, 0, QTableWidgetItem(str(i.id)))
            self.research_person_table_tw.setItem(row_position, 1, QTableWidgetItem(i.convert_date()))
            self.research_person_table_tw.setItem(row_position, 2, QTableWidgetItem(i.person.surname))
            self.research_person_table_tw.setItem(row_position, 3, QTableWidgetItem(i.person.name))
            self.research_person_table_tw.setItem(row_position, 4, QTableWidgetItem(i.person.middle_name))
            self.research_person_table_tw.setItem(row_position, 5, QTableWidgetItem(i.person.convert_date()))
            self.research_person_table_tw.setItem(row_position, 6, QTableWidgetItem(i.person.birthplace))
            number = None
            formation_date = None
            plot = None
            if i.event.case_type == 'criminal':
                number = f'у/д № {i.event.criminal.number}'
                formation_date = i.event.criminal.convert_date()
                plot = i.event.criminal.plot
            elif i.event.case_type == 'incident':
                number = f'КУСП № {i.event.incident.number}'
                formation_date = i.event.incident.convert_date()
                plot = i.event.incident.plot
            elif i.event.case_type == 'requisition':
                number = f'исх. № {i.event.requisition.number}'
                formation_date = i.event.requisition.convert_date()
            self.research_person_table_tw.setItem(row_position, 7, QTableWidgetItem(number))
            self.research_person_table_tw.setItem(row_position, 8, QTableWidgetItem(formation_date))
            self.research_person_table_tw.setItem(row_position, 9, QTableWidgetItem(plot))

    def verify_official_person(self):
        if self.official_person_data_initiator.name_le.text() and \
                self.official_person_data_executor.name_le.text() and \
                self.official_person_data_addresses.name_le.text():
            self.add_person.setEnabled(True)
        else:
            self.add_person.setDisabled(True)

    def create_person(self):
        self.person_data_form = PersonaReferralForm()
        event = self.person_data_form.exec()
        if event:
            self.data = self.person_data_form.get_info()
            self.load_research()
            self.form_research_table()

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
        )
        if self.data['case_category'] != 'requisition':
            event_data.update(
                address=self.data['address'],
                article=self.data['item'],
                plot=self.data['plot']
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


    def create_research_blanks(self):
        indexes = self.research_person_table_tw.selectionModel().selectedRows(0)
        for i in indexes:
            item = Research.get_by_id(i.data())

            doc = DocxTemplate("word_templates/research_referral_person_template.docx")
            context_to_qr = dict(
                organization=item.initiator.department.title(),
                addr_post=item.addressees.post.title(),
                addr_department=item.addressees.department,
                addr_rank=item.addressees.rank,
                addr_name=item.addressees.create_name_reduction(),
                case=item.event.get_event_by_case()['number_to_string'],
                formation_date=item.event.get_event_by_case()['case'].convert_date(),
                article=item.event.get_event_by_case()['case'].article,
                plot=item.event.get_event_by_case()['case'].plot,
                surname=item.person.surname,
                name=item.person.name,
                middle_name=item.person.middle_name,
                birthday=item.person.convert_date(),
                birthplace=item.person.birthplace,
                red_name=item.person.create_name_reduction(),
                init_post=item.initiator.post.title(),
                init_rank=item.initiator.rank,
                init_name=item.initiator.create_name_reduction()
            )
            json_obj = json.dumps(context_to_qr, indent=4, ensure_ascii=False)  # ensure_ascii=False
            print(len(str(json_obj)))
            img = qrcode.make(json_obj)
            img.save('qr_image/qr_image.png')
            image = InlineImage(doc, image_descriptor='qr_image/qr_image.png', width=Mm(50), height=Mm(50))
            context_to_qr['qr'] = image
            doc.render(context_to_qr)
            docs_name = '{}_{}_{}_{}'.format(item.id, context_to_qr['surname'], context_to_qr['name'],
                                             context_to_qr['middle_name'])
            doc.save(f"research_directions/{docs_name}.docx")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ResearchWindow()
    w.show()
    sys.exit(app.exec())
