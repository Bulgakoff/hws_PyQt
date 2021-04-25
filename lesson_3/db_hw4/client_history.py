
from sqlalchemy import Column, Integer, String, \
    exists, and_, select, DateTime
from sqlalchemy.exc import IntegrityError

from db_hw4.base import Base

import sys
from icecream import ic
from sqlalchemy.orm import sessionmaker

class ClientHistory(Base):
    __tablename__='connect_history'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    ip_address = Column(String(4+4+4+3), unique=True)
    when = Column(DateTime)

class ClientHistoryStorage:
    def __init__(self,session):
        self._session = session

    def add_record(self, client_id,address,tm):
        with self._session.begin():
            self._session.add(ClientHistory(client_id=client_id,
                                            address=address,
                                            when=tm))


