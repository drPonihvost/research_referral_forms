import json
import sys

import qrcode
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage

from UI.interface.main_official_person_data_widget import OfficialPersonData
from UI.interface.person_data_form import PersonaReferralForm
from UI.ui_py.research_main_window import Ui_research_main_window
from data_base.models import Research, PersonToCheck, Event


class ResearchWindow(QMainWindow, Ui_research_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.research_person_table_tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.person_data_form = None
        self.data = dict()
        self.official_person_data_initiator = OfficialPersonData(role='initiator')
        self.initiator_lo.addWidget(self.official_person_data_initiator)
        self.official_person_data_addresses = OfficialPersonData(role='addressees')
        self.addressee_lo.addWidget(self.official_person_data_addresses)
        self.official_person_data_executor = OfficialPersonData(role='executor')
        self.executor_lo.addWidget(self.official_person_data_executor)
        self.form_research_table()
        self.activate_button()

        # signals
        self.add_person.clicked.connect(self.create_research)
        self.change_pb.clicked.connect(self.update_research)
        self.delete_pb.clicked.connect(self.delete_research)
        self.official_person_data_executor.choice_pb.clicked.connect(self.activate_button)
        self.official_person_data_addresses.choice_pb.clicked.connect(self.activate_button)
        self.official_person_data_initiator.choice_pb.clicked.connect(self.activate_button)
        self.form_pb.clicked.connect(self.create_research_blanks)
        self.research_person_table_tw.itemSelectionChanged.connect(self.activate_button)

    def activate_button(self):
        off_person = False
        if self.official_person_data_initiator.name_le.text() and \
                self.official_person_data_executor.name_le.text() and \
                self.official_person_data_addresses.name_le.text():
            self.add_person.setEnabled(True)
            off_person = True
        else:
            self.add_person.setEnabled(False)
        enabled = True if self.research_person_table_tw.selectionModel().selectedRows() else False
        self.form_pb.setEnabled(enabled)
        bulk_select = True if len(self.research_person_table_tw.selectionModel().selectedRows()) == 1 else False
        self.change_pb.setEnabled(enabled and bulk_select and off_person)
        self.delete_pb.setEnabled(enabled and bulk_select)

    def toggle_radio_button(self, case_type):
        action = {
            'criminal': self.person_data_form.ud_rb.setChecked,
            'incident': self.person_data_form.kusp_rb.setChecked,
            'requisition': self.person_data_form.req_rb.setChecked
        }
        action[case_type](True)

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
            self.research_person_table_tw.setItem(row_position, 7, QTableWidgetItem(i.event.number_to_string()))
            self.research_person_table_tw.setItem(row_position, 8, QTableWidgetItem(i.event.convert_date()))
            self.research_person_table_tw.setItem(row_position, 9, QTableWidgetItem(i.event.plot))

    def create_research(self):
        self.person_data_form = PersonaReferralForm()
        if self.remember_cb.isChecked():
            record = Research.get_last_record()
            if record:
                self.autofill(record)
        event = self.person_data_form.exec()
        if event:
            self.data = self.person_data_form.get_info()
            research = self.load_research()
            research.save()
            self.form_research_table()
        self.activate_button()

    def update_research(self):
        self.person_data_form = PersonaReferralForm()
        research_id = self.research_person_table_tw.selectionModel().selectedRows(0)[0].data()
        record = Research.get_by_id(research_id)
        if record:
            self.autofill(record)
            event = self.person_data_form.exec()
            if event:
                self.data = self.person_data_form.get_info()
                changed_record = self.change_research(record)
                changed_record.update()
                self.form_research_table()
        self.activate_button()

    def delete_research(self):
        research_id = self.research_person_table_tw.selectionModel().selectedRows(0)[0].data()
        record = Research.get_by_id(research_id)
        event_id = record.event.id
        person_id = record.person.id
        event = Research.get_by_other_person(event_id, person_id)
        if record:
            record.delete()
            if not event:
                Event.get_by_id(event_id).delete()
        self.form_research_table()

    def autofill(self, record):
        if self.sender().objectName() == 'change_pb':
            self.person_data_form.surname_le.setText(record.person.surname)
            self.person_data_form.name_le.setText(record.person.name)
            self.person_data_form.middle_name_le.setText(record.person.middle_name)
            if not record.person.male:
                self.person_data_form.female_rb.toggle()
            self.person_data_form.date_of_birth_de.setDate(record.person.birthday)
            self.person_data_form.birthplace_le.setText(record.person.birthplace)
        self.toggle_radio_button(record.event.case_type)
        self.person_data_form.set_event_type()
        self.person_data_form.event_description_form.number_cb.setText(record.event.number)
        self.person_data_form.event_description_form.formation_date_le.setDate(record.event.formation_date)
        self.person_data_form.plot_te.setText(record.event.plot)
        if record.event.case_type != 'requisition':
            self.person_data_form.event_description_form.item_de.setCurrentText(record.event.article)
            self.person_data_form.event_description_form.number_cb_2.setText(record.event.address)

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
            case_type=self.data['case_category'],
            number=self.data['number'],
            formation_date=self.data['formation_date'],
        )
        event_data.update(
            address=self.data['address'] if self.data['case_category'] != 'requisition' else '',
            article=self.data['item'] if self.data['case_category'] != 'requisition' else '',
            plot=self.data['plot']
        )
        event = Event.get_event_by_data(
            case_type=event_data['case_type'],
            number=event_data['number'],
            formation_date=event_data['formation_date']
        )
        if not event:
            event = Event(**event_data)
        research.person = person
        research.event = event
        return research

    def change_research(self, record):
        addressees_id = self.official_person_data_addresses.official_person_id
        executor_id = self.official_person_data_executor.official_person_id
        initiator_id = self.official_person_data_initiator.official_person_id
        record.addressees_id = addressees_id
        record.executor_id = executor_id
        record.initiator_id = initiator_id
        record.person.surname = self.data['surname']
        record.person.name = self.data['name']
        record.person.middle_name = self.data['middle_name']
        record.person.birthday = self.data['date_of_birth']
        record.person.birthplace = self.data['birthplace']
        record.person.male = self.data['male']
        record.event.case_type = self.data['case_category']
        record.event.number = self.data['number']
        record.event.formation_date = self.data['formation_date']
        record.event.address = self.data['address'] if self.data['case_category'] != 'requisition' else ''
        record.event.article = self.data['item'] if self.data['case_category'] != 'requisition' else ''
        record.event.plot = self.data['plot']
        return record

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
                case=item.event.number_to_string(),
                formation_date=item.event.convert_date(),
                article=item.event.article,
                plot=item.event.plot,
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
        self.activate_button()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ResearchWindow()
    w.show()
    sys.exit(app.exec())
