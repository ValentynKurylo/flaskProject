from datetime import datetime

from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Student, Teacher
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import yaml

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
#s = Session()


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


#def load_yaml():
   #with session_scope() as s:
       #for data in yaml.load_all(open('students.yaml')):
           #student = Student(**data)
           #s.add(student)


if __name__ == '__main__':
    #recreate_database()
    #add_data()

    student = Student(
            name='Valentyn',
            lastname='Kurylo',
            group='KN-215',
            raiting=60
    )
    with session_scope() as s:
        s.add(student)

    student = Student(
        name='Vale',
        lastname='Kur',
        group='KN-215',
        raiting=80
    )
    with session_scope() as s:
        s.add(student)


#def load_yaml():
   #with session_scope() as s:
       #for data in yaml.load_all(open('teachers.yaml')):
           #teacher = Teacher(**data)
           #s.add(teacher)


#if __name__ == '__main__':
   #recreate_database()
   #add_data()

    teacher = Teacher(
            name='Ivan',
            lastname='Mart'

    )
    with session_scope() as s:
        s.add(teacher)