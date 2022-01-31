import os
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, UniqueConstraint, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_NAME = 'test_db.db'
engine = create_engine(f'sqlite:///{os.path.dirname(__file__)}\\{DATABASE_NAME}')
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
        return self

    @staticmethod
    def update():
        session.commit()

    def delete(self, commit=True):
        session.delete(self)
        if commit:
            try:
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    @staticmethod
    def bulk_delete(objects: list):
        for obj in objects:
            session.delete(obj)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


class Research(BaseModel):
    __tablename__ = 'research'

    date_of_recording = Column(DateTime, default=datetime.utcnow)
    date_of_change = Column(DateTime, default=datetime.utcnow)
    date_of_dispatch = Column(DateTime)
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    initiator_id = Column(Integer, ForeignKey('initiator.id'))
    executor_id = Column(Integer, ForeignKey('executor.id'))
    addressee_id = Column(Integer, ForeignKey('addressee.id'))
    dir_path = Column(String, default=None)
    file_name = Column(String, default=None)
    event = relationship('Event', backref='research')
    initiator = relationship('Initiator', backref='research')
    executor = relationship('Executor', backref='research')
    addressee = relationship('Addressee', backref='research')

    @classmethod
    def get_last_record(cls):
        return session.query(cls).order_by(cls.id).desc().first()

    @classmethod
    def get_by_event(cls, event_id):
        return session.query(cls).filter_by(event_id=event_id).first()

    @classmethod
    def get_by_off_person(cls, off_person_id):
        return session.query(cls).filter(or_(cls.initiator_id == off_person_id,
                                             cls.addressee_id == off_person_id,
                                             cls.executor_id == off_person_id)).first()

    def convert_recording_date(self):
        return self.date_of_recording.strftime('%d.%m.%Y')

    def convert_change_date(self):
        return self.date_of_recording.strftime('%d.%m.%Y')

    def convert_dispatch_date(self):
        if self.date_of_dispatch:
            return self.date_of_dispatch.strftime('%d.%m.%Y')


class Person(BaseModel):
    __abstract__ = True
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)

    def create_name_reduction(self):
        return f'{self.surname} {self.name[0].title()}.{self.patronymic[0].title()}.'


class PersonToCheck(Person):
    __tablename__ = 'person_to_check'
    birthday = Column(DateTime)
    birthplace = Column(String)
    male = Column(Boolean, nullable=False)
    reg_place = Column(String)
    img_path = Column(String, default=None)
    research_id = Column(Integer, ForeignKey('research.id'))
    research = relationship('Research', backref='person_to_check')

    @classmethod
    def get_count_by_research(cls, research_id):
        return session.query(cls).filter_by(research_id=research_id).count()

    @classmethod
    def get_by_research(cls, research_id):
        return session.query(cls).filter_by(research_id=research_id).all()

    def get_gender(self):
        return 'Мужской' if self.male else 'Женский'

    def convert_date(self):
        return self.birthday.strftime('%d.%m.%Y')


class Division(BaseModel):
    __tablename__ = 'division'
    __table_args__ = (UniqueConstraint('division_red_name', 'person', name='_division_person'),)
    division_full_name = Column(String)
    division_red_name = Column(String)
    person = Column(String)

    @classmethod
    def get_by_full_and_red_name(cls, division_red_name, division_full_name, person):
        return session.query(cls).filter(
            cls.division_red_name == division_red_name,
            cls.division_full_name == division_full_name,
            cls.person == person
        ).first()

    @classmethod
    def get_by_red_name(cls, division_red_name, person):
        return session.query(cls).filter(
            cls.division_red_name == division_red_name,
            cls.person == person
        ).first()

    @classmethod
    def get_by_person(cls, person):
        return session.query(cls).filter_by(person=person).all()


class OfficialPerson(Person):
    __abstract__ = True
    post = Column(String)
    rank = Column(String)

    def create_name_reduction(self):
        return f'{self.name[0].title()}.{self.patronymic[0].title()}. {self.surname}'


class Initiator(OfficialPerson):
    __tablename__ = 'initiator'

    division_id = Column(Integer, ForeignKey('division.id'))
    division = relationship('Division', backref='initiator')

    @classmethod
    def get_by_division(cls, division_id):
        return session.query(cls).filter_by(division_id=division_id).first()


class Executor(OfficialPerson):
    __tablename__ = 'executor'

    division_id = Column(Integer, ForeignKey('division.id'))
    division = relationship('Division', backref='executor')

    @classmethod
    def get_by_division(cls, division_id):
        return session.query(cls).filter_by(division_id=division_id).first()


class Addressee(OfficialPerson):
    __tablename__ = 'addressee'

    division_id = Column(Integer, ForeignKey('division.id'))
    division = relationship('Division', backref='addressee')

    @classmethod
    def get_by_division(cls, division_id):
        return session.query(cls).filter_by(division_id=division_id).first()


class Event(BaseModel):
    __tablename__ = 'event'
    case_type = Column(String)
    number = Column(String)
    formation_date = Column(DateTime)
    incident_date = Column(DateTime)
    article = Column(String)
    address = Column(String)
    plot = Column(String)

    def convert_formation_date(self):
        if not self.formation_date:
            return ''
        return self.formation_date.strftime('%d.%m.%Y')

    def convert_incident_date(self):
        if not self.incident_date:
            return ''
        return self.incident_date.strftime('%d.%m.%Y')

    def number_to_string(self):
        case = {
            'criminal': 'у/д № ',
            'incident': 'КУСП № ',
            'search_case': 'РД № ',
            'inspection_material': 'Материалы проверки № ',
            'other': ''
        }
        return case[self.case_type] + self.number

    @classmethod
    def get_event_by_data(cls, case_type, number, formation_date: DateTime):
        return session.query(cls).filter(cls.case_type == case_type,
                                         cls.number == number,
                                         cls.formation_date == formation_date).first()


def init_db():
    path = os.path.dirname(__file__)
    if not os.path.exists(f'{path}\\{DATABASE_NAME}'):
        Base.metadata.create_all(engine)
    else:
        Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
