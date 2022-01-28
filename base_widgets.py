from PySide6.QtGui import QFont, QGuiApplication, QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QFormLayout, QLineEdit, \
    QPlainTextEdit, QTableWidget, \
    QAbstractItemView

CASE = ('105. Убийство',
        '106. Убийство матерью новорожденного ребенка',
        '107. Убийство, совершенное в состоянии аффекта',
        '108. Убийство, совершенное при превышении пределов необходимой обороны либо при превышении мер, необходимых для задержания лица, совершившего преступление',
        '109. Причинение смерти по неосторожности',
        'Статья отсутствует'
    )


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


class LineEditWithTip(QLineEdit, BaseWidget):
    def __init__(self, tip: str = ''):
        super().__init__()
        self.tip = tip
        self.setPlaceholderText(tip)
        self.setFont(QFont("Times New Roman", 10, QFont.Cursive))


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
                         'Адрес места проичшествия', 'Событие', 'ст. УК РФ', 'Количество лиц', 'Дата формирования',
                         'Инициатор', 'Адресат',
                         'Исполнитель')

        self.setColumnCount(len(_HEADER_ITEMS))
        self.setHorizontalHeaderLabels(_HEADER_ITEMS)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    def resize_to_content(self):
        self.resizeColumnsToContents()
        self.setColumnWidth(5, 250)
        self.setColumnWidth(6, 300)

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
        self.resizeRowsToContents()


class PersonTableForWizard(PersonTable):
    def __init__(self):
        super().__init__()
        _HEADER_ITEMS = ('Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Пол', 'Место рождения', 'Место пребывания',
                         'Идентификатор')

        self.setColumnCount(len(_HEADER_ITEMS))
        self.setHorizontalHeaderLabels(_HEADER_ITEMS)


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
        self.setColumnWidth(4, 270)
        self.resizeRowsToContents()


class EventTable(QTableWidget, BaseWidget):
    def __init__(self):
        super().__init__()
        _HEADER_ITEMS = ('Номер', 'Дата регистрации', 'Происшествие', 'Дата происшествия', 'Адрес происшествия',
                         'Статья', 'Идентификатор')

        self.setColumnCount(len(_HEADER_ITEMS))
        self.setHorizontalHeaderLabels(_HEADER_ITEMS)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setColumnHidden(6, True)

    def resize_to_content(self):
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setColumnWidth(2, 300)
        self.setColumnWidth(4, 300)
        self.resizeRowsToContents()
