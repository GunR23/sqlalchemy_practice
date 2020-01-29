from sqlalchemy import Column, Integer, String

from database.models.base import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))

    @staticmethod
    def create_book(title, author, genre):
        return Book(title=title, author=author, genre=genre)

