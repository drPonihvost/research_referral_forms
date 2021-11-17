from data_base.models import *


def db_init():

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
