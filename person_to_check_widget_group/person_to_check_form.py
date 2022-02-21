import datetime

from PySide6.QtWidgets import QLabel, QHBoxLayout, QRadioButton

from base_widgets import BaseForm, LineEditWithTip, DateLineEdit
from error_widget import ErrorWidget
from models import PersonToCheck, Research


class PersonToCheckForm(BaseForm):
    __NOMINATIVE_CASE = dict(
        surname_tip='Иванов',
        name_tip='Иван',
        patronymic_tip='Иванович',
        birthplace_tip='Республика Хакасия, г. Абакан',
        related='Мать (Отец)',
        reg_place_tip='Республика Хакасия, г. Абакан, ул. Ленина, д. 12'
    )

    @property
    def nominative_tips(self):
        return self.__NOMINATIVE_CASE

    def __init__(self, research):
        super().__init__()
        self._research = research

        # layout
        self.gender_layout = QHBoxLayout()

        # input elements
        self.surname_le = LineEditWithTip(tip=self.nominative_tips['surname_tip'])
        self.name_le = LineEditWithTip(tip=self.nominative_tips['name_tip'])
        self.patronymic_le = LineEditWithTip(tip=self.nominative_tips['patronymic_tip'])
        self.birthday_le = DateLineEdit()
        self.related_le = LineEditWithTip(tip=self.nominative_tips['related'])
        self.birthplace_le = LineEditWithTip(tip=self.nominative_tips['birthplace_tip'])
        self.reg_place_le = LineEditWithTip(tip=self.nominative_tips['reg_place_tip'])

        # button elements
        self.male_radio = QRadioButton('Мужской')
        self.male_radio.setChecked(True)
        self.female_radio = QRadioButton('Женский')

        # configuration
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.cancel_button)
        self.gender_layout.addWidget(self.male_radio)
        self.gender_layout.addWidget(self.female_radio)
        self.form_layout.addRow(QLabel('Фамилия:'), self.surname_le)
        self.form_layout.addRow(QLabel('Имя:'), self.name_le)
        self.form_layout.addRow(QLabel('Отчество:'), self.patronymic_le)
        self.form_layout.addRow(QLabel('Пол:'), self.gender_layout)
        self.form_layout.addRow(QLabel('Дата рождения:'), self.birthday_le)
        self.form_layout.addRow(QLabel('Место рождения:'), self.birthplace_le)
        if research.related_search:
            self.form_layout.addRow(QLabel('Кем приходится:'), self.related_le)
        self.form_layout.addRow(QLabel('Место пребывания:'), self.reg_place_le)

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        # signal
        self.surname_le.textChanged.connect(self.activate_button)
        self.name_le.textChanged.connect(self.activate_button)
        self.patronymic_le.textChanged.connect(self.activate_button)
        self.birthday_le.textChanged.connect(self.activate_button)
        self.birthplace_le.textChanged.connect(self.activate_button)

        # action
        self.center_and_set_the_size(0.25, 0)
        self.activate_button()

    # slots
    @staticmethod
    def convert_date(date: str):
        f = '%d.%m.%Y'
        return datetime.datetime.strptime(date, f).date()

    def activate_button(self) -> None:
        self.add_button.setEnabled(False)
        print(self.validate_field())
        if self.validate_field():
            self.add_button.setEnabled(True)

    def validate_field(self) -> bool:
        v_list = [
            True if self.surname_le.text() else False,
            True if self.name_le.text() else False,
            True if self.patronymic_le.text() else False,
            True if self.birthday_le.get_date() else False,
            True if self.birthplace_le.text() else False
        ]
        if self._research.related_search:
            v_list.append(True if self.related_le.text() else False)
        return False not in v_list

    def fill_the_form(self, person: PersonToCheck):
        self.surname_le.setText(person.surname)
        self.name_le.setText(person.name)
        self.patronymic_le.setText(person.patronymic)
        self.birthday_le.setText(person.convert_date())
        self.birthplace_le.setText(person.birthplace)
        self.reg_place_le.setText(person.reg_place)
        self.related_le.setText(person.related)

    def get_data(self):
        related = None
        if self._research.related_search:
            related = self.related_le.text()
        return dict(
            surname=self.surname_le.text(),
            name=self.name_le.text(),
            patronymic=self.patronymic_le.text(),
            male=True if self.male_radio.isChecked() else False,
            birthday=self.convert_date(self.birthday_le.text()),
            birthplace=self.birthplace_le.text(),
            related=related,
            reg_place=self.reg_place_le.text(),
            research=self._research
        )

    def date_validator(self) -> str or None:
        if not self.birthday_le.get_date():
            return f'Дата рождения: не верный формат даты'
        if self.birthday_le.get_date() > datetime.datetime.now():
            return f'Дата рождения не корректна'

    def accept(self) -> None:
        error = self.date_validator()
        if error:
            error_widget = ErrorWidget(title='Ошибка валидации', text=error)
            error_widget.exec()
            return
        super().accept()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = PersonToCheckForm(Research.get_by_id(3))
    w.show()
    sys.exit(app.exec())