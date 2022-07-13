from configparser import ConfigParser

from DbRepo import DbRepo
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# user-name: postgres
# password: admin
# database: test_db


config = ConfigParser()
config.read("config2.conf")
connection_string = config["db"]["connection_string"]

Base1 = declarative_base()

engine = create_engine(connection_string, echo=True)


def create_all_entities():
    Base1.metadata.create_all(engine)


Session = sessionmaker()

local_session2 = Session(bind=engine)


db_repo = DbRepo(local_session2)
