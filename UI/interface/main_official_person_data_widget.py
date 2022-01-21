from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QAbstractItemView

from UI.ui_py.create_official_person_dialog import Ui_create_official_person_dialog
from UI.ui_py.official_person_choice_dialog import Ui_official_person_choice
from UI.ui_py.official_person_data_widget import Ui_official_person_data
from data_base.models import Addressee, Executor, Initiator, Research


class CreateOfficialPersonDialog(QDialog, Ui_create_official_person_dialog):
    def __init__(self, role):
        super().__init__()
        self.role = role
        self.table = dict(
            addressees=Addressee,
            executor=Executor,
            initiator=Initiator
        )
        self.setupUi(self)

        # Signals
        self.accept_pb.clicked.connect(self.accept)
        self.cancel_pb.clicked.connect(self.reject)

    def get_data(self):
        return {
            'department': self.department_te.toPlainText(),
            'post': self.post_te.toPlainText(),
            'rank': self.rank_le.text(),
            'surname': self.surname_le.text(),
            'name': self.name_le.text(),
            'middle_name': self.middle_name_le.text()
        }


class OfficialPersonChoice(QDialog, QWidget, Ui_official_person_choice):
    def __init__(self, role):
        super().__init__()
        self.role = role
        self.table = dict(
            addressees=Addressee,
            executor=Executor,
            initiator=Initiator
        )
        self.setupUi(self)
        self.official_person_tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.official_person_tw.setSelectionMode(QAbstractItemView.SingleSelection)
        self.form_table()
        self.activate_button()
        self.create_person_widget = None

        # Signals
        self.select_pb.clicked.connect(self.accept)
        self.cancel_pb.clicked.connect(self.reject)
        self.add_pb.clicked.connect(self.add_official_person)
        self.change_pb.clicked.connect(self.change_official_person)
        self.delete_pb.clicked.connect(self.delete_official_person)
        self.official_person_tw.itemSelectionChanged.connect(self.activate_button)

    def activate_button(self):
        enabled = True if self.official_person_tw.selectionModel().selectedRows(0) else False
        self.select_pb.setEnabled(enabled)
        self.change_pb.setEnabled(enabled)
        self.delete_pb.setEnabled(enabled)

    def form_table(self):
        self.official_person_tw.setRowCount(0)
        table = self.table[self.role]
        off_person = table.get_all()
        if off_person:
            for i in off_person:
                row_position = self.official_person_tw.rowCount()
                self.official_person_tw.insertRow(row_position)
                self.official_person_tw.setItem(row_position, 0, QTableWidgetItem(str(i.id)))
                self.official_person_tw.setItem(row_position, 1, QTableWidgetItem(i.create_name_reduction()))
                self.official_person_tw.setItem(row_position, 2, QTableWidgetItem(i.post))
                self.official_person_tw.setItem(row_position, 3, QTableWidgetItem(i.department))
                self.official_person_tw.setItem(row_position, 4, QTableWidgetItem(i.rank))

    def add_official_person(self):
        self.create_person_widget = CreateOfficialPersonDialog(self.role)
        event = self.create_person_widget.exec()
        if event:
            data = self.create_person_widget.get_data()
            official_person = self.table[self.role](**data)
            official_person.save()
            self.form_table()
        self.activate_button()

    def change_official_person(self):
        item_id = int(self.get_item_id())
        item = self.table[self.role].get_by_id(item_id)
        self.create_person_widget = CreateOfficialPersonDialog(self.role)
        self.create_person_widget.department_te.setText(item.department)
        self.create_person_widget.post_te.setText(item.post)
        self.create_person_widget.rank_le.setText(item.rank)
        self.create_person_widget.name_le.setText(item.name)
        self.create_person_widget.surname_le.setText(item.surname)
        self.create_person_widget.middle_name_le.setText(item.patronymic)
        event = self.create_person_widget.exec()
        if event:
            data = self.create_person_widget.get_data()
            item.department = data['department']
            item.post = data['post']
            item.rank = data['rank']
            item.name = data['name']
            item.surname = data['surname']
            item.patronymic = data['middle_name']
            item.update()
            self.form_table()
        self.activate_button()

    def delete_official_person(self):
        item_id = int(self.get_item_id())
        item = self.table[self.role].get_by_id(item_id)
        research = Research.get_by_off_person_id(role=self.role, off_person_id=item_id)
        if research:
            print('Удаление невозможно есть связанные направления')
        else:
            item.delete()
        self.form_table()
        self.activate_button()

    def get_item_id(self):
        return self.official_person_tw.selectedItems()[0].text()


class OfficialPersonData(QWidget, Ui_official_person_data):
    def __init__(self, role):
        super().__init__()
        self.role = role
        self.table = dict(
            addressees=Addressee,
            executor=Executor,
            initiator=Initiator
        )
        self.official_person_id = None
        self.setupUi(self)
        if role == 'addressees':
            self.oficial_person_lb.setText('Адресат')
        elif role == 'executor':
            self.oficial_person_lb.setText('Исполнитель')
        elif role == 'initiator':
            self.oficial_person_lb.setText('Инициатор')

        self.select_person_widget = None

        # signals
        self.choice_pb.clicked.connect(self.select_person_widget_call)

    def select_person_widget_call(self):
        self.select_person_widget = OfficialPersonChoice(self.role)
        event = self.select_person_widget.exec()
        if event:
            self.official_person_id = int(self.select_person_widget.get_item_id())
            table = self.table[self.role]
            item = table.get_by_id(self.official_person_id)
            self.department_te.setText(item.department)
            self.post_te.setText(item.post)
            self.rank_le.setText(item.rank)
            self.name_le.setText(item.create_name_reduction())
        elif not self.table[self.role].get_all():
            self.department_te.clear()
            self.post_te.clear()
            self.rank_le.clear()
            self.name_le.clear()
