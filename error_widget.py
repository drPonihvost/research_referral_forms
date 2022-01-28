from PySide6.QtWidgets import QMessageBox

from base_widgets import BaseWidget


class ErrorWidget(QMessageBox, BaseWidget):
    def __init__(self, title, text):
        super().__init__()
        self.center_and_set_the_size(0.13, 0.17)
        self.setWindowTitle(title)
        self.setText(text)

