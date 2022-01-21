import sys

from PySide6.QtWidgets import QApplication

from UI.interface.research_widget import ResearchWidget
from data_base.models import init_db


class MainWindow(ResearchWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_db()
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
