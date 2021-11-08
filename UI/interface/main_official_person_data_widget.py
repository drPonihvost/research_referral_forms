import sys

from PySide6.QtWidgets import QApplication, QWidget, QDialog, QTableWidgetItem, QAbstractItemView

from UI.ui_py.create_official_person_dialog import Ui_create_official_person_dialog
from UI.ui_py.official_person_choice_dialog import Ui_official_person_choice
from UI.ui_py.official_person_data_widget import Ui_official_person_data

n = '1'

data = dict(
    department='ЭКЦ МВД по Республике Хакасия',
    post='Начальник',
    rank='полковник полиции',
    name='Лысенко Т.М.'
)

official_person = {
    n: data
}


class CreateOfficialPersonDialog(QDialog, Ui_create_official_person_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Signals
        self.accept_pb.clicked.connect(self.accept)
        self.cancel_pb.clicked.connect(self.reject)

    def get_data(self):
        return {
            'department': self.department_te.toPlainText(),
            'post': self.post_te.toPlainText(),
            'rank': self.rank_le.text(),
            'name': self.name_le.text()
        }


class OfficialPersonChoice(QDialog, QWidget, Ui_official_person_choice):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.official_person_tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.official_person_tw.setSelectionMode(QAbstractItemView.SingleSelection)
        self.form_table()
        self.create_person_widget = None

        # Signals
        self.select_pb.clicked.connect(self.accept)
        self.cancel_pb.clicked.connect(self.reject)
        self.add_pb.clicked.connect(self.add_official_person)
        self.change_pb.clicked.connect(self.change_official_person)
        self.delete_pb.clicked.connect(self.delete_official_person)

    def form_table(self):
        self.official_person_tw.setRowCount(0)
        if official_person:
            for key, value in official_person.items():
                row_position = self.official_person_tw.rowCount()
                self.official_person_tw.insertRow(row_position)
                self.official_person_tw.setItem(row_position, 0, QTableWidgetItem(key))
                self.official_person_tw.setItem(row_position, 1, QTableWidgetItem(value['name']))
                self.official_person_tw.setItem(row_position, 2, QTableWidgetItem(value['post']))
                self.official_person_tw.setItem(row_position, 3, QTableWidgetItem(value['department']))
                self.official_person_tw.setItem(row_position, 4, QTableWidgetItem(value['rank']))

    def add_official_person(self):
        self.create_person_widget = CreateOfficialPersonDialog()
        event = self.create_person_widget.exec()
        if event:
            global n
            n = str(int(n) + 1)
            official_person[n] = self.create_person_widget.get_data()
            self.form_table()

    def change_official_person(self):
        item_id = self.get_item_id()
        self.create_person_widget = CreateOfficialPersonDialog()
        self.create_person_widget.department_te.setText(official_person[item_id]['department'])
        self.create_person_widget.post_te.setText(official_person[item_id]['post'])
        self.create_person_widget.rank_le.setText(official_person[item_id]['rank'])
        self.create_person_widget.name_le.setText(official_person[item_id]['name'])
        event = self.create_person_widget.exec()
        if event:
            official_person[item_id] = self.create_person_widget.get_data()
            print(official_person)
            self.form_table()

    def delete_official_person(self):
        item_id = self.get_item_id()
        official_person.pop(item_id)
        self.form_table()


    def get_item_id(self):
        return self.official_person_tw.selectedItems()[0].text()


class OfficialPersonData(QWidget, Ui_official_person_data):
    def __init__(self, role):
        super().__init__()
        self.role = role
        role_dict = dict(
            initiator='Инициатор',
            addresses='Адресат',
            executor='Исполнитель'
        )
        self.setupUi(self)
        self.oficial_person_lb.setText(role_dict[self.role])

        self.select_person_widget = None

        # signals
        self.choice_pb.clicked.connect(self.select_person_widget_call)

    def select_person_widget_call(self):
        self.select_person_widget = OfficialPersonChoice()
        event = self.select_person_widget.exec()
        if event:
            item_id = self.select_person_widget.get_item_id()
            self.department_te.setText(official_person[item_id]['department'])
            self.post_te.setText(official_person[item_id]['post'])
            self.rank_le.setText(official_person[item_id]['rank'])
            self.name_le.setText(official_person[item_id]['name'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = OfficialPersonData(role='initiator')
    w.show()
    sys.exit(app.exec())
