from sqlalchemy import Column, Integer, \
    String, exists, and_, select, engine, create_engine
from sqlalchemy.exc import IntegrityError

from db_hw4.base import Base
from db_hw4.client_history import ClientHistoryStorage
import sys
from icecream import ic
from sqlalchemy.orm import sessionmaker
from db_hw4.client import ClientStorage


if __name__ == '__main__':
    engine = create_engine('sqlite:///qwe_sqlite1.db')
    Base.metadata.create_all(engine) # создает все
    # таблицы что обнаружил
    Session = sessionmaker(bind=engine)

    with Session() as session:
        client_storage = ClientStorage(session)
        client_storage.client_add('foo','PaSsWord')
        exists = client_storage.client_exists('foo','PaSsWord')

        ic(exists)



