import json
import os

from datetime import datetime

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QFont, QGuiApplication, QRegularExpressionValidator, QMouseEvent
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QFormLayout, QLineEdit, \
    QPlainTextEdit, QTableWidget, \
    QAbstractItemView, QComboBox


class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFont(QFont("Times New Roman", 10, QFont.Normal))

    def center_and_set_the_size(self, x_ratio: float = 1, y_ratio: float = 1) -> None:
        desktop = QGuiApplication.screens()[0].geometry()
        desktop_width = desktop.width()
        desktop_height = desktop.height()
        self.resize(desktop.width() * x_ratio, desktop.height() * y_ratio)

        x = (desktop_width - desktop.width() * x_ratio) // 2
        y = (desktop_height - desktop.height() * y_ratio) // 2
        self.move(x, y)
        self.show()


class BaseForm(QDialog, BaseWidget):
    def __init__(self):
        super().__init__()

        # layout
        self.main_layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.form_layout.setVerticalSpacing(10)
        self.button_layout = QHBoxLayout()

        # button elements
        self.add_button = QPushButton('Добавить')
        self.cancel_button = QPushButton('Отмена')

        # signal
        self.add_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)


class ArticleCombo(QComboBox, BaseWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(350)
        self.addItems(self.get_config())

    @staticmethod
    def get_config():
        with open(os.path.join(os.path.dirname(__file__), 'initial_data.json'), 'r', encoding='utf-8') as json_data:
            data = json.load(json_data)['config']['case']
            return data


class LineEditWithTip(QLineEdit, BaseWidget):
    def __init__(self, tip: str = ''):
        super().__init__()
        self.tip = tip
        self.setPlaceholderText(tip)
        self.setFont(QFont("Times New Roman", 10, QFont.Cursive))


class LineEditForCriminalCase(QLineEdit, BaseWidget):
    def __init__(self):
        super().__init__()
        reg_ex = QRegularExpression(r"\d{17}")
        input_validator = QRegularExpressionValidator(reg_ex, self)
        self.setValidator(input_validator)


class DateLineEdit(QLineEdit, BaseWidget):
    def __init__(self):
        super().__init__()
        self.setInputMask("00.00.0000")
        self.setMaximumWidth(120)

    def mousePressEvent(self, arg__1: QMouseEvent) -> None:
        super().mousePressEvent(arg__1)
        self.home(False)

    def get_date(self) -> datetime or None:
        try:
            date = datetime.strptime(self.text(), '%d.%m.%Y')
            return date
        except ValueError:
            return

    def set_date(self, date: datetime or None) -> None:
        self.setText('')
        if date:
            self.setText(date.strftime('%d.%m.%Y'))


class PlainTextEditTabAction(QPlainTextEdit, BaseWidget):
    def __init__(self):
        super().__init__()
        self.setTabChangesFocus(True)


class OfficialPersonButton(QPushButton, BaseWidget):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setMaximumWidth(110)


class ResearchTable(QTableWidget, BaseWidget):
    def __init__(self):
        super().__init__()
        _HEADER_ITEMS = ('Идентификатор', 'Дата создания', 'Дата изменения', 'Основание', ' Дата происшествия',
                         'Адрес места проишествия', 'Событие', 'ст. УК РФ', 'Родственный поиск', 'Количество лиц',
                         'Дата формирования', 'Инициатор', 'Адресат', 'Исполнитель')

        self.setColumnCount(len(_HEADER_ITEMS))
        self.setHorizontalHeaderLabels(_HEADER_ITEMS)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    def resize_to_content(self):
        self.resizeColumnsToContents()
        self.setColumnWidth(5, 250)
        self.setColumnWidth(6, 250)
        self.setColumnWidth(7, 250)
        self.setColumnHidden(0, True)
        self.resizeRowsToContents()


class PersonTable(QTableWidget, BaseWidget):
    def __init__(self):
        super().__init__()
        _HEADER_ITEMS = ('Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Пол', 'Место рождения', 'Место пребывания',
                         'Идентификатор', 'Основание проверки', 'Направлен на проверку')

        self.setColumnCount(len(_HEADER_ITEMS))
        self.setHorizontalHeaderLabels(_HEADER_ITEMS)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setColumnHidden(7, True)

    def resize_to_content(self):
        self.resizeColumnsToContents()
        self.setColumnWidth(5, 200)
        self.setColumnWidth(6, 200)
        self.resizeRowsToContents()


class PersonTableForWizard(PersonTable):
    def __init__(self):
        super().__init__()
        _HEADER_ITEMS = ('Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Пол', 'Родственник', 'Место рождения',
                         'Место пребывания', 'Идентификатор')

        self.setColumnCount(len(_HEADER_ITEMS))
        self.setHorizontalHeaderLabels(_HEADER_ITEMS)
        self.setColumnHidden(8, True)


class OfficialPersonTable(QTableWidget, BaseWidget):
    def __init__(self, person):
        super().__init__()

        _HEADER_ITEMS = ('ФИО', 'Подразделение', 'Должность', 'Спец. звание', 'Полное наименование подразделения',
                         'Идентификатор')

        self.person = person

        self.setColumnCount(len(_HEADER_ITEMS))
        self.setHorizontalHeaderLabels(_HEADER_ITEMS)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    def resize_to_content(self):
        self.resizeColumnsToContents()
        self.setColumnWidth(1, 250)
        self.setColumnWidth(2, 150)
        self.setColumnWidth(3, 150)
        self.setColumnWidth(4, 250)
        self.resizeRowsToContents()


class EventTable(QTableWidget, BaseWidget):
    def __init__(self):
        super().__init__()
        _HEADER_ITEMS = ('Идентификатор', 'Номер', 'Дата регистрации', 'Происшествие', 'Дата происшествия', 'Адрес происшествия',
                         'Статья')

        self.setColumnCount(len(_HEADER_ITEMS))
        self.setHorizontalHeaderLabels(_HEADER_ITEMS)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setColumnHidden(0, True)

    def resize_to_content(self):
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setColumnWidth(2, 250)
        self.setColumnWidth(4, 250)
        self.setColumnWidth(5, 250)
        self.resizeRowsToContents()
