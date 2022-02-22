from PySide2.QtWidgets import QMessageBox

from base_widgets import BaseWidget


class ErrorWidget(QMessageBox, BaseWidget):
    def __init__(self, title, text=''):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)
        self.center_and_set_the_size(0.13, 0.17)

    def set_error_list(self, error_list):
        text = str()
        for error in enumerate(error_list, start=1):
            text += f'{error[0]}: {error[1]}\n'
        self.setText(text)



