import sys

from PySide6.QtWidgets import QDialog, QApplication
from base_widgets import BaseWidget


class AddEventDialog(QDialog, BaseWidget):
    def __init__(self):
        super().__init__()
        self.center_and_set_the_size(0.4, 0.8)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AddEventDialog()
    sys.exit(app.exec())
