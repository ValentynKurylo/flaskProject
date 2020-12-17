from crud import Session
from models import Student, Teacher

s = Session()

students = s.query(Student).all()

