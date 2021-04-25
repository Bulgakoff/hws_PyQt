from icecream import ic
from sqlalchemy import Integer, Table, Column, ForeignKey, \
    create_engine, String, select
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
friendship = Table(
    'friendships', Base.metadata,
    Column('friend_a_id', Integer, ForeignKey('users.id'),
           primary_key=True),
    Column('friend_b_id', Integer, ForeignKey('users.id'),
           primary_key=True)
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # this relationship is used for persistence
    friends = relationship("User", secondary=friendship,
                           primaryjoin=id == friendship.c.friend_a_id,
                           secondaryjoin=id == friendship.c.friend_b_id,
                           )

    def __repr__(self):
        return f"User {self.name}, friends ====={friendship_union}"


# this relationship is viewonly and selects across the union of all
# friends
friendship_union = select([
    friendship.c.friend_a_id,
    friendship.c.friend_b_id
]).union(
    select([
        friendship.c.friend_b_id,
        friendship.c.friend_a_id]
    )
).alias()
User.all_friends = relationship('User',
                                secondary=friendship_union,
                                primaryjoin=User.id == friendship_union.c.friend_a_id,
                                secondaryjoin=User.id == friendship_union.c.friend_b_id,
                                viewonly=True)
e = create_engine("sqlite:///anketa_3.db")
Base.metadata.create_all(e)
s = Session(e)
u1, u2, u3, u4, u5 = User(name='u1'), User(name='u2'), \
                     User(name='u3'), User(name='u4'), User(name='u5')
u1.friends = [u2, u3]
u4.friends = [u2, u5]
u3.friends.append(u5)
s.add_all([u1, u2, u3, u4, u5])
s.commit()
ic(u2.all_friends)

ic(u5.all_friends)
