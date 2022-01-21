from datetime import datetime

from PySide6.QtWidgets import QWizard, QWizardPage, QVBoxLayout
from UI.interface.base_widgets import BaseWidget
from UI.interface.official_person_widget import OfficialPersonWidget
from data_base.models import Research


class FormBlankWizard(QWizard, BaseWidget):
    def __init__(self, research_id):
        super().__init__()
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
            initiator_id=self.page(0).get_off_person_id(),
            addressee_id=self.page(1).get_off_person_id(),
            executor_id=self.page(0).get_off_person_id()
        )


class OfficialPersonPage(QWizardPage, BaseWidget):
    def __init__(self, off_person_id, off_person):
        super().__init__()
        param = dict(
            initiator=('Инициатор', 'Выберите инициатора'),
            addressee=('Адресат', 'Выберите адресата'),
            executor=('Исполнитель', 'Выберите исполнителя')
        )
        self.off_person_id = off_person_id
        self.setSubTitle(param[off_person][0])
        self.setTitle(param[off_person][1])
        self.widget = OfficialPersonWidget(off_person)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.widget)
        self.setLayout(self.layout)

        # signals
        self.widget.table.itemSelectionChanged.connect(self.activate_button)

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

    def get_off_person_id(self):
        return self.widget.table.item(self.widget.table.currentRow(), 5).text()


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    wizard = FormBlankWizard(1)
    wizard.show()
    sys.exit(app.exec())
