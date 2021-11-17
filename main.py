import sys

from PySide6.QtWidgets import QApplication

from data_base.db_init import db_init

from UI.interface.main_window import ResearchWindow


class MainWindow(ResearchWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db_init()
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
