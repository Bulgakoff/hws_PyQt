import sys
from icecream import ic
from sqlalchemy import Column, ForeignKey, Integer, String, \
    exists, and_, DateTime, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import Engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

#
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    Name = Column(String)
    children = relationship("Child", back_populates="parent")

    def __init__(self, name):
        self.Name = name

    def __repr__(self):
        return "<Parent ('%s')>" % self.Name


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    Name = Column(String)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")

    def __init__(self, name, parent_id):
        self.Name = name
        self.parent_id = parent_id

    def __repr__(self):
        return "<Child ('%s')>" % self.Name


if __name__ == '__main__':
    engine = create_engine('sqlite:///qwe_sqlite2.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    parent_user = Parent("vasia")
    ic("Classic Mapping. parent_user: ", parent_user)

    child_user = Child("Alexxx", 1)
    ic("Classic Mapping. child_user: ", child_user)
    session.add(parent_user)
    session.add(child_user)

    session.add_all(
        [
            Parent("zina"),
            Child("kolia", 5),
        ]
    )

    q_user = session.query(Parent).filter_by(Name="vasia") \
        .first()
    ic("Simple query:", q_user)
    session.commit()
