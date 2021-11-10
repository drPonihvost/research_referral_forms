import inspect
import os
import sys
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_NAME = 'test_db.db'


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


engine = create_engine(f'sqlite:///{get_script_dir()}\\{DATABASE_NAME}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class BaseDBModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

    def save(self, commit=True):
        session.add(self)
        if commit:
            try:
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    @staticmethod
    def update():
        session.commit()

    def delete(self, commit=True):
        session.delete(self)
        if commit:
            session.commit()


class Research(BaseDBModel):
    __tablename__ = 'research'
    date_of_recording = Column(DateTime, default=datetime.utcnow)
    person_id = Column(Integer, ForeignKey('person_to_check.id'), nullable=False)
    initiator_id = Column(Integer, ForeignKey('initiator.id'), nullable=False)
    executor_id = Column(Integer, ForeignKey('executor.id'), nullable=False)
    addressees_id = Column(Integer, ForeignKey('addressees.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    person = relationship('PersonToCheck', backref='research')
    initiator = relationship('Initiator', backref='research')
    executor = relationship('Executor', backref='research')
    addressees = relationship('Addressees', backref='research')
    event = relationship('Event', backref='research')

    @classmethod
    def get_all(cls):
        return session.query().all()


class Person(BaseDBModel):
    __abstract__ = True
    surname = Column(String)
    name = Column(String)
    middle_name = Column(String)

    def __init__(self, surname, name, middle_name):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name

    @classmethod
    def get_by_id(cls, item_id):
        return session.query(cls).get(item_id)


class PersonToCheck(Person):
    __tablename__ = 'person_to_check'
    birthday = Column(DateTime)
    birthplace = Column(String)
    male = Column(Boolean, nullable=False)

    def __init__(self, surname, name, middle_name, birthday, birthplace, male):
        super().__init__(surname, name, middle_name)
        self.birthday = birthday
        self.birthplace = birthplace
        self.male = male


class OfficialPerson(Person):
    __abstract__ = True
    post = Column(String)
    rank = Column(String)
    department = Column(String)

    def __init__(self, surname, name, middle_name, post, rank, department):
        super().__init__(surname, name, middle_name)
        self.post = post
        self.rank = rank
        self.department = department

    def __repr__(self):
        return f'{self.id} {self.surname} {self.name} {self.middle_name} {self.post} {self.rank} {self.department}'

    @classmethod
    def get_all_name(cls):
        return session.query(cls).all()

    def create_name_reduction(self):
        return f'{self.name[0].title()}.{self.middle_name[0].title()}. {self.surname}'


class Initiator(OfficialPerson):
    __tablename__ = 'initiator'


class Executor(OfficialPerson):
    __tablename__ = 'executor'


class Addressees(OfficialPerson):
    __tablename__ = 'addressees'


class Event(BaseDBModel):
    __tablename__ = 'event'
    case_type = Column(String)
    criminal_id = Column(Integer, ForeignKey('criminal.id'))
    incident_id = Column(Integer, ForeignKey('incident.id'))
    requisition_id = Column(Integer, ForeignKey('requisition.id'))
    search_case_id = Column(Integer, ForeignKey('search_case.id'))
    inspection_material_id = Column(Integer, ForeignKey('inspection_material.id'))
    criminal = relationship('Criminal', backref='event')
    incident = relationship('Incident', backref='event')
    requisition = relationship('Requisition', backref='event')
    search_case = relationship('SearchCase', backref='event')
    inspection_material = relationship('InspectionMaterial', backref='event')

    def __init__(self, case_type):
        self.case_type = case_type


class Case(BaseDBModel):
    __abstract__ = True
    number = Column(String)
    formation_date = Column(DateTime)

    def __init__(self, number, formation_date):
        self.number = number
        self.formation_date = formation_date


class Requisition(Case):
    __tablename__ = 'requisition'


class BaseIncident(Case):
    __abstract__ = True
    article = Column(String)
    address = Column(String)
    incident = Column(Text)

    def __init__(self, number, formation_date, article, address, incident):
        super().__init__(number, formation_date)
        self.article = article
        self.address = address
        self.incident = incident


class Criminal(BaseIncident):
    __tablename__ = 'criminal'


class Incident(BaseIncident):
    __tablename__ = 'incident'


class SearchCase(BaseIncident):
    __tablename__ = 'search_case'


class InspectionMaterial(BaseIncident):
    __tablename__ = 'inspection_material'


def init_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()
