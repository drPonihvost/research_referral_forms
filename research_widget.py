import os
import shutil

import qrcode

from PySide6 import QtCore, QtPrintSupport, QtWebChannel, QtWebEngineCore
from PySide6.QtCore import QMarginsF
from PySide6.QtGui import QPageLayout, QPageSize
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem
from jinja2 import Template

from base_widgets import BaseWidget, ResearchTable
from error_widget import ErrorWidget
from form_blank_wizard import FormBlankWizard
from research_wizard import ResearchWizard
from models import Research, PersonToCheck
from html_templates import HTML_PERSON


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

        # signals
        self.add_research_pb.clicked.connect(self.create_research)
        self.change_research_pb.clicked.connect(self.edit_research)
        self.delete_research_pb.clicked.connect(self.delete_research)
        self.form_research_pb.clicked.connect(self.form_blank)
        self.table.itemSelectionChanged.connect(self.activate_button)

        # actions
        self.table.resize_to_content()
        self.fill_the_table(Research.get_all())
        self.activate_button()

    # slots
    def activate_button(self):
        enabled = True if self.table.selectionModel().selectedRows(0) else False
        self.change_research_pb.setEnabled(enabled)
        self.form_research_pb.setEnabled(enabled)
        self.delete_research_pb.setEnabled(enabled)

    def fill_the_table(self, researches: list[Research]):
        self.table.setRowCount(0)
        if not researches:
            return
        for research in reversed(researches):
            persons_to_check_count = PersonToCheck.get_count_by_research(research.id)
            initiator = research.initiator.create_name_reduction() if research.initiator else ''
            executor = research.executor.create_name_reduction() if research.initiator else ''
            addressee = research.addressee.create_name_reduction() if research.initiator else ''
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

    def create_research(self):
        wizard = ResearchWizard()
        wizard.exec()
        self.fill_the_table(Research.get_all())
        self.activate_button()

    def edit_research(self):
        research_id = self.table.item(self.table.currentRow(), 0).text()
        wizard = ResearchWizard(research_id)
        event = wizard.exec()
        if event:
            research = Research.get_by_id(research_id)
            research.initiator_id = None
            research.addressee_id = None
            research.executor_id = None
            research.date_of_dispatch = None
            research.update()
        self.fill_the_table(Research.get_all())
        self.activate_button()

    def delete_research(self):
        research_id = self.table.item(self.table.currentRow(), 0).text()
        persons_to_check = PersonToCheck.get_by_research(research_id)
        PersonToCheck.bulk_delete(persons_to_check)
        Research.delete(Research.get_by_id(research_id))
        self.fill_the_table(Research.get_all())
        self.activate_button()

    def init_dispatch(self):
        research = None
        research_id = self.table.item(self.table.currentRow(), 0).text()
        wizard = FormBlankWizard(research_id)
        event = wizard.exec()
        if event:
            research = Research.get_by_id(research_id)
            data = wizard.get_off_persons_id()
            research.date_of_dispatch = data['date_of_dispatch']
            research.initiator_id = data['initiator_id']
            research.addressee_id = data['addressee_id']
            research.executor_id = data['executor_id']
            research.update()
        return research

    @staticmethod
    def create_main_res_dir():
        main_res_dir = os.path.dirname(__file__) + '\\research_blanks'
        if not os.path.exists(main_res_dir):
            os.mkdir(main_res_dir)
        return main_res_dir

    def create_research_dir(self, research):
        file_name = self.create_file_name(research)
        research_dir = os.path.dirname(__file__) + '\\research_blanks' + f'\\{file_name}'
        os.mkdir(research_dir)
        research.dir_path = research_dir
        research.file_name = file_name
        research.update()

    @staticmethod
    def create_file_name(research):
        return f'{research.id}_{research.convert_dispatch_date()}_{research.event.number}_{research.executor.create_name_reduction()}'

    def set_research_dir(self, research):
        if not research.dir_path:
            self.create_research_dir(research)
            return
        if os.path.exists(research.dir_path):
            shutil.rmtree(research.dir_path)
            self.create_research_dir(research)

    @staticmethod
    def create_event_qr(research: Research) -> None:
        event = research.event
        event_to_qr = event.number_to_string() + '*' + \
                      event.convert_formation_date() + '*' + \
                      event.convert_incident_date() + '*' + \
                      ('' if not event.article else event.article) + '*' + \
                      ('' if not event.address else event.address) + '*' + \
                      ('' if not event.plot else event.plot)
        event_to_qr = event_to_qr.encode('utf-8')
        img = qrcode.make(event_to_qr)
        img.save(research.dir_path + '\\event.png')

    @staticmethod
    def create_initiator_qr(research: Research) -> None:
        initiator = research.initiator
        initiator_to_qr = initiator.division.division_full_name + '*' + \
            initiator.division.division_red_name + '*' + \
            initiator.surname + '*' + \
            initiator.name + '*' + \
            initiator.patronymic + '*' + \
            initiator.post + '*' + \
            initiator.rank
        initiator_to_qr = initiator_to_qr.encode('utf-8')
        img = qrcode.make(initiator_to_qr)
        img.save(research.dir_path + '\\initiator.png')

    @staticmethod
    def create_executor_qr(research: Research) -> None:
        executor = research.executor
        executor_to_qr = executor.division.division_full_name + '*' + \
                          executor.division.division_red_name + '*' + \
                          executor.surname + '*' + \
                          executor.name + '*' + \
                          executor.patronymic + '*' + \
                          executor.post + '*' + \
                          executor.rank
        executor_to_qr = executor_to_qr.encode('utf-8')
        img = qrcode.make(executor_to_qr)
        img.save(research.dir_path + '\\executor.png')

    @staticmethod
    def create_person_qr(research: Research, persons_to_check: list[PersonToCheck]) -> None:
        persons_dir = research.dir_path + '\\person'
        os.mkdir(persons_dir)
        for person in persons_to_check:
            filename = f'{person.id}_{person.create_name_reduction()}_{person.convert_date()}.png'
            person_to_qr = person.surname + '*' + \
                           person.name + '*' + \
                           person.patronymic + '*' + \
                           person.convert_date() + '*' + \
                           person.birthplace + '*' + \
                           person.get_gender()
            person_to_qr = person_to_qr.encode('utf-8')
            img = qrcode.make(person_to_qr)
            img.save(persons_dir + '\\' + filename)
            person.img_path = persons_dir + '\\' + filename
            person.update()

    @staticmethod
    def get_data_by_pdf(research: Research, persons_to_check: list[PersonToCheck]) -> dict:
        persons = persons_to_check
        return dict(
            name='МВД РОССИИ',
            regional_department='МИНИСТЕРСТВО ВНУТРЕННИХ ДЕЛ РОССИИ ПО РЕСПУБЛИКЕ ХАКАСИЯ',
            department_address='',
            research=research,
            persons=persons
        )

    def fill_html_template(self, research: Research, template: str, persons_to_check: list[PersonToCheck]):
        data = self.get_data_by_pdf(research, persons_to_check)
        template = Template(template)
        rendered_page = template.render(**data)
        with open(research.dir_path + '\\' + research.file_name + '.html', "w", encoding="UTF-8") as fh:
            fh.write(rendered_page)

    def create_pdf(self, research: Research, persons_to_check: list[PersonToCheck]) -> None:
        self.fill_html_template(research, HTML_PERSON, persons_to_check)
        page = QWebEnginePage()
        page.load(QtCore.QUrl.fromLocalFile(research.dir_path + f'\\{research.file_name}.html'))

        def handle_load_finished(status):
            if status:
                param = QPageLayout(QPageSize(QPageSize.A4), QPageLayout.Portrait, QMarginsF())
                param.setUnits(QPageLayout.Millimeter)
                param.setRightMargin(20.0)
                param.setLeftMargin(20.0)
                param.setTopMargin(20.0)
                param.setBottomMargin(15.0)
                page.printToPdf(research.dir_path + f'\\{research.file_name}.pdf', param)
        page.loadFinished.connect(handle_load_finished)

    def form_blank(self):
        person_to_check = PersonToCheck.get_count_by_research(self.table.item(self.table.currentRow(), 0).text())
        if not person_to_check:
            message = ErrorWidget(
                text='''Нельзя сформировать направление
                без лиц''',
                title='Ошибка формирования'
            )
            message.exec()
        else:
            self.create_main_res_dir()
            research = self.init_dispatch()
            if research:
                self.set_research_dir(research)
                self.create_event_qr(research)
                self.create_initiator_qr(research)
                self.create_executor_qr(research)
                self.create_person_qr(research, PersonToCheck.get_by_research(research.id))
                self.create_pdf(research, PersonToCheck.get_by_research(research.id))
            self.fill_the_table(Research.get_all())
        self.activate_button()
