from data_base.models import *

create_db()

addressees = Addressees(
    department='ЭКЦ МВД по Республике Хакасия',
    post='Начальник',
    rank='полковник полиции',
    surname='Лысенко',
    name='Тимур',
    middle_name='Михайлович'
)
addressees.save()