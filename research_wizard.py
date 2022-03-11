from datetime import datetime

from PySide2.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QLineEdit

from base_widgets import BaseWidget, DateLineEdit
from event_widget_group.event_widget import EventWidget
from person_to_check_widget_group.person_to_check_widget_for_wizard import PersonToCheckWidgetForWizard
from models import Research, Event


class ResearchWizard(QWizard, BaseWidget):
    def __init__(self, research=None, related=False):
        super().__init__()
        self.set_window_config()
        self.research = research
        self.related = related
        if research:
            self.setWindowTitle('Изменить направление на исследование')
        else:
            self.setWindowTitle('Создать направление на исследование')
        self.addPage(ResearchPage(self.research))
        self.addPage(EventPage(self.research, self.related))
        self.addPage(PersonPage(self.research))
        self.setButtonText(QWizard.BackButton, 'Назад')
        self.setButtonText(QWizard.NextButton, 'Далее')
        self.setButtonText(QWizard.CancelButton, 'Отмена')
        self.setButtonText(QWizard.FinishButton, 'Готово')
        self.setWizardStyle(QWizard.ModernStyle)

        self.center_and_set_the_size(0.6, 0.5)


class ResearchPage(QWizardPage, BaseWidget):
    def __init__(self, research):
        super().__init__()
        self.research = research
        self.date_le = DateLineEdit()
        self.setTitle('Установите дату создания направления:')
        self.registerField('date', self.date_le)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.date_le)
        self.setLayout(self.layout)
        if self.research:
            self.edit_research()
        else:
            self.add_research()

    def add_research(self):
        self.date_le.set_date(datetime.utcnow())

    def edit_research(self):
        self.date_le.set_date(self.research.date_of_recording)


class EventPage(QWizardPage, BaseWidget):
    def __init__(self, research, related):
        super().__init__()
        self.setTitle('Выберите или создайте событие:')
        self.date_of_record = None
        self.research_id = None
        self.research = research
        self.related = related
        self.widget = EventWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.widget)
        self.setLayout(self.layout)
        if self.research:
            self.select_row()
        self.widget.table.itemSelectionChanged.connect(self.activate_button)

    @staticmethod
    def convert_date(date: str):
        f = '%d.%m.%Y'
        return datetime.strptime(date, f).date()

    def activate_button(self):
        self.wizard().button(QWizard.NextButton).setEnabled(self.isComplete())

    def isComplete(self) -> bool:
        return True if self.widget.table.selectionModel().selectedRows(0) else False

    def get_event(self):
        event_id = self.widget.table.item(self.widget.table.currentRow(), 0).text()
        return Event.get_by_id(event_id)

    def select_row(self):
        if self.research:
            self.widget.set_data(self.research.event)

    def edit_research(self):
        self.research.date_of_recording = self.convert_date(self.date_of_record)
        self.research.date_of_change = datetime.utcnow()
        self.research.event = self.get_event()
        self.research.update()

    def add_research(self):
        research = Research(
            date_of_recording=self.convert_date(self.date_of_record),
            date_of_change=datetime.utcnow(),
            event=self.get_event(),
            related_search=self.related
        ).save()
        self.research = research
        self.research_id = QLineEdit(str(self.research.id))
        self.registerField('research_id', self.research_id)

    def initializePage(self) -> None:
        super().initializePage()
        self.date_of_record = self.field('date')
        self.select_row()


class PersonPage(QWizardPage):
    def __init__(self, research):
        super().__init__()
        self.setTitle('Занесите в таблицу все лица направленные на проверку по текущему событию:')
        self.research = research
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def initializePage(self) -> None:
        super().initializePage()
        if not self.wizard().page(1).research:
            self.wizard().page(1).add_research()
            self.research = self.wizard().page(1).research
        else:
            self.wizard().page(1).edit_research()
        self.set_widget()

    def set_widget(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()
        if self.research:
            widget = PersonToCheckWidgetForWizard(self.research)
            widget.table.setColumnHidden(5, not self.research.related_search)
            self.layout.addWidget(widget)