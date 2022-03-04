import sys

from PySide2.QtWidgets import QApplication

from main_window import MainWindow
from models import init_db


class Window(MainWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_db()
    w = Window()
    w.show()
    sys.exit(app.exec_())
