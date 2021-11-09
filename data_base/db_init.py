import os
import sys
import inspect

from data_base.models import *


Base.metadata.drop_all(engine)
init_db()

addressees = Addressees(
    department='ЭКЦ МВД по Республике Хакасия',
    post='Начальник',
    rank='полковник полиции',
    surname='Лысенко',
    name='Тимур',
    middle_name='Михайлович'
)
addressees.save()