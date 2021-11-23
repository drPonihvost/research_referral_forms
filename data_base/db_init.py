from data_base.models import *
import os


def db_init():
    path = os.path.dirname(__file__)
    if not os.path.exists(f'{path}\\{DATABASE_NAME}'):
        init_db()
        Addressees(
            department='ЭКЦ МВД по Республике Хакасия',
            post='Начальник',
            rank='полковник полиции',
            surname='Лысенко',
            name='Тимур',
            middle_name='Михайлович'
        ).save()
        Initiator(
            department='ОМВД России по Таштыпскому району',
            post='Начальник',
            rank='полковник полиции',
            surname='Грачев',
            name='Александр',
            middle_name='Александрович'
        ).save()
        Executor(
            department='ОУР ОМВД России по Таштыпскому району',
            post='Оперуполномоченный',
            rank='капитан полиции',
            surname='Пупкин',
            name='Василий',
            middle_name='Васильевич'
        ).save()
    else:
        init_db()


