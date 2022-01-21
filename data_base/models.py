import os
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, extract
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_NAME = 'test_db.db'

# def get_script_dir(follow_symlinks=True):
#     if getattr(sys, 'frozen', False):
#         path = os.path.abspath(sys.executable)
#     else:
#         path = inspect.getabsfile(get_script_dir)
#     if follow_symlinks:
#         path = os.path.realpath(path)
#     return os.path.dirname(path)


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
    event = relationship('Event', backref='research')
    initiator = relationship('Initiator', backref='research')
    executor = relationship('Executor', backref='research')
    addressee = relationship('Addressee', backref='research')

    @classmethod
    def get_last_record(cls):
        return session.query(cls).order_by(cls.id).desc().first()

    def convert_recording_date(self):
        return self.date_of_recording.strftime('%d.%m.%Y')

    def convert_change_date(self):
        return self.date_of_recording.strftime('%d.%m.%Y')

    def convert_dispatch_date(self):
        if self.date_of_dispatch:
            return self.date_of_recording.strftime('%d.%m.%Y')


class Person(BaseModel):
    __abstract__ = True
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)

    # def __init__(self, surname, name, patronymic):
    #     self.surname = surname
    #     self.name = name
    #     self.patronymic = patronymic

    def create_name_reduction(self):
        return f'{self.surname} {self.name[0].title()}.{self.patronymic[0].title()}.'


class PersonToCheck(Person):
    __tablename__ = 'person_to_check'
    birthday = Column(DateTime)
    birthplace = Column(String)
    male = Column(Boolean, nullable=False)
    reg_place = Column(String)
    research_id = Column(Integer, ForeignKey('research.id'))
    research = relationship('Research', backref='person_to_check')

    # def __init__(self, surname, name, patronymic, birthday, birthplace, male, research, reg_place):
    #     super().__init__(surname, name, patronymic)
    #     self.birthday = birthday
    #     self.birthplace = birthplace
    #     self.male = male
    #     self.reg_place = reg_place
    #     self.research = research

    @classmethod
    def get_count_by_research(cls, research_id):
        return session.query(cls).filter_by(research_id=research_id).count()

    @classmethod
    def get_by_research(cls, research_id):
        return session.query(cls).filter_by(research_id=research_id).all()

    def convert_date(self):
        return self.birthday.strftime('%d.%m.%Y')

    def get_gender(self):
        return 'Мужской' if self.male else 'Женский'


class Division(BaseModel):
    __tablename__ = 'division'
    division_full_name = Column(String)
    division_red_name = Column(String, unique=True)
    person = Column(String)

    # def __init__(self, division_full_name, division_red_name, person):
    #     self.division_full_name = division_full_name
    #     self.division_red_name = division_red_name
    #     self.person = person

    @classmethod
    def get_by_full_and_red_name(cls, division_red_name, division_full_name, person):
        return session.query(cls).filter(
            cls.division_red_name == division_red_name,
            cls.division_full_name == division_full_name,
            cls.person == person
        ).first()

    @classmethod
    def get_by_red_name(cls, division_red_name,  person):
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

    # def __init__(self, surname, name, patronymic, post, rank):
    #     super().__init__(surname, name, patronymic)
    #     self.post = post
    #     self.rank = rank

    def create_name_reduction(self):
        return f'{self.name[0].title()}.{self.patronymic[0].title()}. {self.surname}'


class Initiator(OfficialPerson):
    __tablename__ = 'initiator'

    division_id = Column(Integer, ForeignKey('division.id'))
    division = relationship('Division', backref='initiator')

    # def __init__(self, surname, name, patronymic, post, rank, division):
    #     super().__init__(surname, name, patronymic, post, rank)
    #     self.division = division


class Executor(OfficialPerson):
    __tablename__ = 'executor'

    division_id = Column(Integer, ForeignKey('division.id'))
    division = relationship('Division', backref='executor')

    # def __init__(self, surname, name, patronymic, post, rank, division):
    #     super().__init__(surname, name, patronymic, post, rank)
    #     self.division = division


class Addressee(OfficialPerson):
    __tablename__ = 'addressee'

    division_id = Column(Integer, ForeignKey('division.id'))
    division = relationship('Division', backref='addressee')

    # def __init__(self, surname, name, patronymic, post, rank, division):
    #     super().__init__(surname, name, patronymic, post, rank)
    #     self.division = division


class Event(BaseModel):
    __tablename__ = 'event'
    case_type = Column(String)
    number = Column(String)
    formation_date = Column(DateTime)
    incident_date = Column(DateTime)
    article = Column(String)
    address = Column(String)
    plot = Column(String)

    # def __init__(self, case_type, number, formation_date, incident_date, article, address, plot):
    #     self.case_type = case_type
    #     self.number = number
    #     self.formation_date = formation_date
    #     self.incident_date = incident_date
    #     self.article = article
    #     self.address = address
    #     self.plot = plot

    def convert_formation_date(self):
        if self.formation_date:
            return self.formation_date.strftime('%d.%m.%Y')

    def convert_incident_date(self):
        if self.incident_date:
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
        addressee = Addressee(
            division=Division(
                division_full_name='Экспертно криминалистический центр МВД по Республике Хакасия',
                division_red_name='ЭКЦ МВД по Республике Хакасия',
                person='addressee'
            ),
            post='Начальнику',
            rank='полковнику полиции',
            surname='Лысенко',
            name='Тимуру',
            patronymic='Михайловичу'
        ).save()
        Addressee(
            division=Division.get_by_red_name(
                division_red_name='ЭКЦ МВД по Республике Хакасия',
                person='addressee'
            ),
            post='Врио начальника',
            rank='полковнику полиции',
            surname='Кузнецову',
            name='Дмитрию',
            patronymic='Александровичу'
        ).save()
        initiator = Initiator(
            division=Division(
                division_full_name='Отдел министерства внутренних дел России по Таштыпскому району',
                division_red_name='ОМВД России по Таштыпскому району',
                person='initiator'
            ),
            post='Начальник',
            rank='полковник полиции',
            surname='Грачев',
            name='Александр',
            patronymic='Александрович'
        ).save()
        executor = Executor(
            division=Division(
                division_full_name='Отдел уголовного розыска МВД России по Таштыпскому району',
                division_red_name='ОУР ОМВД России по Таштыпскому району',
                person='executor'
            ),
            post='Оперуполномоченный',
            rank='капитан полиции',
            surname='Пупкин',
            name='Василий',
            patronymic='Васильевич'
        ).save()
        Research(
            event=Event(
                case_type='criminal',
                number='12101950003000045',
                formation_date=datetime(2021, 3, 17, 0, 0, 0),
                incident_date=datetime(2021, 3, 19, 0, 0, 0),
                article='158',
                address='Республика Хакасия, Таштыпский район, с. Таштып, ул. Березовая, д. 2',
                plot='Кража коровы принадлежащей Иванову Т.А.',
            )
        ).save()
        research = Research(
            event=Event(
                case_type='incident',
                number='45612',
                formation_date=datetime(2021, 8, 23, 0, 0, 0),
                incident_date=datetime(2021, 8, 23, 0, 0, 0),
                article='158',
                address='Республика Хакасия, Таштыпский район, с. Таштып, Мира, д. 2',
                plot='Кража мотоцикла принадлежащего Романову А.А. с проникновением в надворную постройку',
            ),
            initiator=initiator,
            executor=executor,
            addressee=addressee,
            date_of_dispatch=datetime(2022, 1, 10, 0, 0, 0)
        )
        PersonToCheck(
            surname='Петров',
            name='Василий',
            patronymic='Иванович',
            birthday=datetime(1991, 11, 24, 0, 0, 0),
            birthplace='Республика Хакасия, Таштыпский район, с. Таштып',
            male=True,
            reg_place='',
            research=research
        ).save()
        PersonToCheck(
            surname='Воротилов',
            name='Дмитрий',
            patronymic='Иванович',
            birthday=datetime(1974, 2, 13, 0, 0, 0),
            birthplace='Республика Хакасия, Таштыпский район, с. Таштып',
            male=True,
            reg_place='',
            research=research
        ).save()
        PersonToCheck(
            surname='Васильев',
            name='Денис',
            patronymic='Викторович',
            birthday=datetime(1993, 7, 15, 0, 0, 0),
            birthplace='Республика Хакасия, Таштыпский район, с. Таштып',
            male=True,
            reg_place='',
            research=research
        ).save()
    else:
        Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()

