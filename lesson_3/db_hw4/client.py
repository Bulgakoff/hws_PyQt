from sqlalchemy import Column, Integer, String, exists, and_, select, event
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError
# для создания отношений между таблицами
from sqlalchemy.orm import relationship
from db_hw4.base import Base
import sys
from icecream import ic
from sqlalchemy.orm import sessionmaker
# для определения таблицы и модели
from sqlalchemy.ext.declarative import declarative_base
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Client(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    password = Column(String(100))

    def __repr__(self):
        return f"<Client(id = '{self.id}')," \
               f" (login = {self.login})," \
               f" (password = {self.password})"


class ClientStorage:
    def __init__(self, session):
        self._session = session

    def client_add(self, login, password):
        try:
            with self._session.begin():
                self._session.add(Client(login=login, password=password))
        except IntegrityError as e:
            raise ValueError('Логин должен быть уникальным') from e

    def client_exists(self, login, password):
        stmt = exists().where(and_(Client.login == login, Client.password == password))
        return self._session.query(Client).filter(stmt).first() != None

    def find(self, client_id):
        """Возвращается  Датакласс с id, login, password"""
        pass