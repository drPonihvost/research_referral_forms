from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem

from base_widgets import BaseWidget, EventTable
from error_widget import ErrorWidget
from event_form import EventForm
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
    def activate_button(self):
        enabled = True if self.table.selectionModel().selectedRows(0) else False
        self.edit_event_pb.setEnabled(enabled)
        self.delete_event_pb.setEnabled(enabled)

    def fill_the_table(self, events: list[Event]):
        self.table.setRowCount(0)
        if not events:
            return
        for event in reversed(events):
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(event.number_to_string()))
            self.table.setItem(row, 1, QTableWidgetItem(event.convert_formation_date()))
            self.table.setItem(row, 2, QTableWidgetItem(event.plot))
            self.table.setItem(row, 3, QTableWidgetItem(event.convert_incident_date()))
            self.table.setItem(row, 4, QTableWidgetItem(event.address))
            self.table.setItem(row, 5, QTableWidgetItem(event.article))
            self.table.setItem(row, 6, QTableWidgetItem(str(event.id)))
        self.table.resize_to_content()

    def add_event(self):
        event_form = EventForm()
        event = event_form.exec()
        if event:
            data = event_form.get_data()
            event = Event.get_event_by_data(
                case_type=data['case_type'],
                number=data['number'],
                formation_date=data['formation_date']
            )
            if not event:
                Event(**data).save()
            else:
                message = ErrorWidget(
                    text='Такая запись уже существует',
                    title='Ошибка добавления'
                )
                message.exec()
        self.fill_the_table(Event.get_all())

    def edit_event(self):
        row = self.table.currentRow()
        event_id = self.table.item(row, 6).text()
        event_db = Event.get_by_id(event_id)
        event_form = EventForm()
        event_form.fill_the_form(event_db)
        event = event_form.exec()
        if event:
            data = event_form.get_data()
            event_db.case_type = data['case_type']
            event_db.number = data['number']
            event_db.formation_date = data['formation_date']
            event_db.incident_date = data['incident_date']
            event_db.article = data['article']
            event_db.address = data['address']
            event_db.plot = data['plot']
            event_db.update()
        self.fill_the_table(Event.get_all())
        self.table.selectRow(row)

    def delete_event(self):
        event_id = self.table.item(self.table.currentRow(), 6).text()
        research = Research.get_by_event(event_id)
        if research:
            message = ErrorWidget(
                text='Это событие связано с направлением на исследование, удаление невозможно.',
                title='Ошибка удаления'
            )
            message.exec()
            return
        event = Event.get_by_id(event_id)
        event.delete()
        self.fill_the_table(Event.get_all())
