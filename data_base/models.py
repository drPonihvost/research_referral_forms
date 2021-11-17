import inspect
import os
import sys
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean
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


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, item_id):
        return session.query(cls).get(item_id)

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


class Research(BaseModel):
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

    def convert_date(self):
        return self.date_of_recording.strftime('%d.%m.%Y')


class Person(BaseModel):
    __abstract__ = True
    surname = Column(String)
    name = Column(String)
    middle_name = Column(String)

    def __init__(self, surname, name, middle_name):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name


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

    def create_name_reduction(self):
        return f'{self.surname} {self.name[0].title()}.{self.middle_name[0].title()}.'

    def convert_date(self):
        return self.birthday.strftime('%d.%m.%Y')


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

    def create_name_reduction(self):
        return f'{self.name[0].title()}.{self.middle_name[0].title()}. {self.surname}'


class Initiator(OfficialPerson):
    __tablename__ = 'initiator'


class Executor(OfficialPerson):
    __tablename__ = 'executor'


class Addressees(OfficialPerson):
    __tablename__ = 'addressees'


class Event(BaseModel):
    __tablename__ = 'event'
    case_type = Column(String)
    number = Column(String)
    formation_date = Column(DateTime)
    article = Column(String)
    address = Column(String)
    plot = Column(String)

    def __init__(self, case_type, number, formation_date, article, address, plot):
        self.case_type = case_type
        self.number = number
        self.formation_date = formation_date
        self.article = article
        self.address = address
        self.plot = plot

    def convert_date(self):
        return self.formation_date.strftime('%d.%m.%Y')

    def number_to_string(self):
        case = {
            'criminal': 'у/д № ',
            'incident': 'КУСП № ',
            'search_case': 'РД № ',
            'inspection_material': '',
            'requisition': 'исх. № '
        }
        return case[self.case_type] + self.number

    @classmethod
    def get_event_by_data(cls, case_type, number):
        return session.query(cls).filter_by(case_type=case_type, number=number).first()

    # def get_event_by_case(self):
    #     case = dict()
    #     case['type'] = self.case_type
    #     if case['type'] == 'criminal':
    #         case['case'] = self.criminal
    #         case['number_to_string'] = f'у/д № {self.criminal.number}'
    #     elif case['type'] == 'incident':
    #         case['case'] = self.incident
    #         case['number_to_string'] = f'КУСП № {self.incident.number}'
    #     elif case['type'] == 'search_case':
    #         case['case'] = self.search_case
    #         case['number_to_string'] = f'РД № {self.search_case.number}'
    #     elif case['type'] == 'inspection_material':
    #         case['case'] = self.inspection_material
    #         case['number_to_string'] = f'{self.inspection_material.number}'
    #     elif case['type'] == 'requisition':
    #         case['case'] = self.requisition
    #         case['number_to_string'] = f'исх. № {self.requisition.number}'
    #     return case


def init_db():
    Base.metadata.create_all(engine)
