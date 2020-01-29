from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models.base import Base
from configuration import DATABASE_CONNECTION_STRING


def connect():
    engine = create_engine(DATABASE_CONNECTION_STRING)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session
