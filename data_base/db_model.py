from sqlalchemy import Column, Integer, String

from data_base.base import Base


class OfficialPersonDBModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    middle_name = Column(String)
    post = Column(String)
    rank = Column(String)
    department = Column(String)

    def __init__(self, surname, name, middle_name, post, rank, department):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.post = post
        self.rank = rank
        self.department = department


class Initiator(OfficialPersonDBModel):
    __table_name__ = 'initiator'


class Executor(OfficialPersonDBModel):
    __table_name__ = 'Executor'


class Addressees(OfficialPersonDBModel):
    __table_name__ = 'Addresses'
