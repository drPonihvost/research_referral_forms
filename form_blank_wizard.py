from datetime import datetime

from PySide6.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QLineEdit
from base_widgets import BaseWidget
from official_person_widget import OfficialPersonWidget
from models import Research


class FormBlankWizard(QWizard, BaseWidget):
    def __init__(self, research_id):
        super().__init__()
        self.setWizardStyle(QWizard.ModernStyle)
        self.research = Research.get_by_id(research_id)
        self.addPage(OfficialPersonPage(self.research.initiator_id, 'initiator'))
        self.addPage(OfficialPersonPage(self.research.addressee_id, 'addressee'))
        self.addPage(OfficialPersonPage(self.research.executor_id, 'executor'))
        self.setButtonText(QWizard.BackButton, 'Назад')
        self.setButtonText(QWizard.NextButton, 'Далее')
        self.setButtonText(QWizard.CancelButton, 'Отмена')
        self.setButtonText(QWizard.FinishButton, 'Готово')
        self.center_and_set_the_size(0.6, 0.5)

    def get_off_persons_id(self):
        return dict(
            date_of_dispatch=datetime.utcnow(),
            initiator_id=self.field('initiator'),
            addressee_id=self.field('addressee'),
            executor_id=self.field('executor')
        )


class OfficialPersonPage(QWizardPage, BaseWidget):
    def __init__(self, off_person_id, off_person):
        super().__init__()
        param = dict(
            initiator=('Инициатор', 'Выберите инициатора:'),
            addressee=('Адресат', 'Выберите адресата:'),
            executor=('Исполнитель', 'Выберите исполнителя:')
        )
        self.off_person_id_le = QLineEdit()
        self.off_person = off_person
        self.off_person_id = off_person_id
        if self.off_person_id:
            self.off_person_id_le.setText(str(self.off_person_id))
        self.registerField(off_person, self.off_person_id_le)
        self.setTitle(param[off_person][1])
        self.widget = OfficialPersonWidget(off_person)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.widget)
        self.setLayout(self.layout)

        # signals
        self.widget.table.itemSelectionChanged.connect(self.set_off_person_id)

    def activate_button(self):
        self.wizard().button(QWizard.NextButton).setEnabled(self.isComplete())
        self.wizard().button(QWizard.FinishButton).setEnabled(self.isComplete())

    def isComplete(self) -> bool:
        return True if self.widget.table.selectionModel().selectedRows(0) else False

    def initializePage(self) -> None:
        if self.off_person_id:
            self.select_row()

    def select_row(self):
        for row in range(self.widget.table.rowCount()):
            if self.widget.table.item(row, 5).text() == str(self.off_person_id):
                self.widget.table.selectRow(row)
                return

    def set_off_person_id(self):
        if self.widget.table.selectionModel().selectedRows(0):
            self.setField(self.off_person, self.widget.table.item(self.widget.table.currentRow(), 5).text())
            self.activate_button()

