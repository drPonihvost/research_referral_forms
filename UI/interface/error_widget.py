import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLabel, QMessageBox

from base_widgets import BaseWidget


class ErrorWidget(QMessageBox, BaseWidget):
    def __init__(self, title, text):
        super().__init__()
        self.center_and_set_the_size(0.13, 0.17)
        self.setWindowTitle(title)
        self.setText(text)

        # configuration


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ErrorWidget()
    w.show()
    sys.exit(app.exec())
