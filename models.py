from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import MONEY

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    group = Column(String)
    raiting = Column(Integer)

    def __repr__(self):
        return "<Student(name='{}', lastname='{}', group={}, raiting={})>" \
            .format(self.name, self.lastname, self.group, self.raiting)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)


    def __repr__(self):
        return "<Student(name='{}', lastname='{}')>" \
            .format(self.name, self.lastname)