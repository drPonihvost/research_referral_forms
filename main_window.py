from PySide6.QtWidgets import QMainWindow, QTabWidget

from base_widgets import BaseWidget
from person_to_check_widget import PersonToCheckWidget
from research_widget import ResearchWidget


class MainWindow(QMainWindow, BaseWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Направления - исследование ДНК')
        self.center_and_set_the_size(0.9, 0.8)

        # widgets
        self.research_widget = ResearchWidget()
        self.person_widget = PersonToCheckWidget()
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(self.research_widget, 'Направления на исследование')
        self.tab_widget.addTab(self.person_widget, 'Лица на проверку')

        # layout
        self.setCentralWidget(self.tab_widget)

