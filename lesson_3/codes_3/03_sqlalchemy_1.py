# ------------------------------ Базы данных -----------------------------

# SQLAlchemy. Часть 1

import sys

# Проверим версию SQLAlchemy
from icecream import ic

try:
    import sqlalchemy

    ic(sqlalchemy.__version__)
except ImportError:
    ic("Библиотека SQLAlchemy не найдена")
    sys.exit(13)

# ----------------------------------------------------------------------------

ic(" ------ Классическое создание таблицы, класса и отображения ------")

# Работа с классическим отображением (Classical Mapping) #
##########################################################

from sqlalchemy import create_engine

# Создадим БД в памяти или в файле
# Флаг `echo` включает ведение лога через стандартный модуль `logging` Питона.
# engine = create_engine("sqlite:///:memory:", echo=True)
engine = create_engine('sqlite:///qwe1.db')

# Импортируем необходимые классы (типы данных, таблицы, метаданные, ключи)
from sqlalchemy import Column, Integer, MetaData, String, Table

# Подготовим "запрос" на создание таблицы users внутри каталога MetaData
metadata = MetaData()
users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("fullname", String),
    Column("password", String),
)

# Выполним запрос CREATE TABLE
metadata.create_all(engine)


# Создадим класс для отображения таблицы БД
class User:
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


# Выполним связывание таблицы и класса-отображения
from sqlalchemy.orm import mapper

m = mapper(User, users_table)
ic("Classic Mapping. Mapper: ", m)

# Создадим объект-пользователя
classic_user = User("Вася", "Василий", "qweasdzxc")
ic("Classic Mapping. User: ", classic_user)
ic("Classic Mapping. User ID: ", classic_user.id)

# ----------------------------------------------------------------------------

ic(" ------ Декларативное создание таблицы и класса ------")

# Декларативное создание таблицы, класса и отображения #
########################################################

# Для использования декларативного стиля необходима функция declarative_base
from sqlalchemy.ext.declarative import declarative_base

# Функция declarative_base создаёт базовый класс для декларативной работы
Base = declarative_base()

# На основании базового класса можно создавать необходимые классы
class DeclarativeUser(Base):
    __tablename__ = "users1111111"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


# Таблица доступна через атрибут класса
users_table = DeclarativeUser.__table__
ic("Declarative. Table:", users_table)
# Метеданные доступны через класс Base
metadata = Base.metadata
ic("Declarative. Metadata:", metadata)
# sys.exit(0)
metadata.create_all(engine)

ic(" ----------------- Работа с сессией ---------------------------------")

#                   Создание сессии                       #
###########################################################

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)


# Класс Session будет создавать Session-объекты, которые привязаны к базе данных
session = Session()
ic("Session:", session)
# sys.exit(0)

#                   Добавление новых объектов                      #
####################################################################

# Для сохранения объекта User, нужно добавить его к имеющейся сессии
admin_user = DeclarativeUser("vasia", "Vasiliy Pypkin", "vasia2000")
session.add(admin_user)

# Объект созданный через классическое отображение
# также сохраняется в БД через сессию
session.add(classic_user)

# Простой запрос
q_user = session.query(User).filter_by(name="vasia").first()
ic("Simple query:", q_user)

# Добавить сразу несколько записей
session.add_all(
    [
        User("kolia", "Cool Kolian[S.A.]", "kolia$$$"),
        User("zina", "Zina Korzina", "zk18"),
    ]
)

# Сессия "знает" об изменениях пользователя
admin_user.password = "-=VP2001=-"
ic("Session. Changed objects:", session.dirty)

# Атрибут `new` хранит объекты, ожидающие сохранения в базу данных
ic("Session. New objects:", session.new)

# Метод commit() фиксирует транзакцию, сохраняя оставшиеся изменения в базу
session.commit()

ic("User ID after commit:", admin_user.id)
