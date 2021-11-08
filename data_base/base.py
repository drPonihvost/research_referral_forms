from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data_base/test_db.db', echo=True)

Base = declarative_base()

