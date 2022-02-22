from typing import List

from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem

from base_widgets import BaseWidget, EventTable
from error_widget import ErrorWidget
from event_widget_group.event_form import EventForm
from models import Event, Research


class EventWidget(BaseWidget):
    def __init__(self):
        super().__init__()

        # layout
        self.main_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()

        # widgets
        self.table = EventTable()

        # buttons
        self.add_event_pb = QPushButton('Добавить')
        self.edit_event_pb = QPushButton('Изменить')
        self.delete_event_pb = QPushButton('Удалить')

        # configuration
        self.button_layout.addWidget(self.add_event_pb)
        self.button_layout.addWidget(self.edit_event_pb)
        self.button_layout.addWidget(self.delete_event_pb)
        self.button_layout.addStretch(0)
        self.table_layout.addWidget(self.table)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.table_layout)
        self.setLayout(self.main_layout)

        # signals
        self.add_event_pb.clicked.connect(self.add_event)
        self.add_event_pb.clicked.connect(self.activate_button)
        self.edit_event_pb.clicked.connect(self.edit_event)
        self.edit_event_pb.clicked.connect(self.activate_button)
        self.delete_event_pb.clicked.connect(self.delete_event)
        self.delete_event_pb.clicked.connect(self.activate_button)
        self.table.itemSelectionChanged.connect(self.activate_button)

        # actions
        self.table.resize_to_content()
        self.fill_the_table(Event.get_all())
        self.activate_button()

    # slots
    def select_row(self, db_event: Event) -> None:
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).text() == str(db_event.id):
                self.table.selectRow(row)
                return

    def set_data(self, db_event: Event = None) -> None:
        self.fill_the_table(Event.get_all())
        if db_event:
            self.select_row(db_event)

    def get_event(self) -> Event:
        event_id = self.table.item(self.table.currentRow(), 0).text()
        return Event.get_by_id(event_id)

    def activate_button(self):
        enabled = True if self.table.selectionModel().selectedRows(0) else False
        self.edit_event_pb.setEnabled(enabled)
        self.delete_event_pb.setEnabled(enabled)

    def fill_the_table(self, events: List[Event]):
        self.table.setRowCount(0)
        if not events:
            return
        for event in reversed(events):
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(event.id)))
            self.table.setItem(row, 1, QTableWidgetItem(event.number_to_string()))
            self.table.setItem(row, 2, QTableWidgetItem(event.convert_formation_date()))
            self.table.setItem(row, 3, QTableWidgetItem(event.plot))
            self.table.setItem(row, 4, QTableWidgetItem(event.convert_incident_date()))
            self.table.setItem(row, 5, QTableWidgetItem(event.address))
            self.table.setItem(row, 6, QTableWidgetItem(event.article))
        self.table.resize_to_content()

    def add_event(self) -> None:
        event_form = EventForm()
        event_form.setup_ui()
        event_form.set_radio('criminal')
        if event_form.exec():
            data = event_form.get_data()
            uniq = event_form.check_for_uniqueness(data)
            if uniq:
                error_widget = ErrorWidget(title='Ошибка записи', text='Такая запись уже существует')
                error_widget.exec()
                return
            db_event = Event(**data).save()
            self.select_row(db_event)
        self.fill_the_table(Event.get_all())

    def edit_event(self):
        db_event = self.get_event()
        event_form = EventForm()
        event_form.setup_ui()
        event_form.set_data(db_event)
        event = event_form.exec()
        if event:
            data = event_form.get_data()
            db_event.case_type = data['case_type']
            db_event.number = data['number']
            db_event.formation_date = data['formation_date']
            db_event.incident_date = data['incident_date']
            db_event.article = data['article']
            db_event.address = data['address']
            db_event.plot = data['plot']
            db_event.update()
        self.fill_the_table(Event.get_all())
        self.select_row(db_event)

    def delete_event(self) -> None:
        db_event = self.get_event()
        research = Research.get_by_event(db_event.id)
        if research:
            message = ErrorWidget(
                text='Это событие связано с направлением на исследование, удаление невозможно.',
                title='Ошибка удаления'
            )
            message.exec()
            self.select_row(db_event)
            return
        db_event.delete()
        self.fill_the_table(Event.get_all())
