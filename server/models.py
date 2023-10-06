from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

# Define the Teacher class
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    salary = Column(Integer)
    classes = relationship('Class', backref='teacher', lazy=True)

# Define the Student class
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    age = Column(Integer)
    grade = Column(Integer)
    classes = relationship('Class', backref='student', lazy=True)

# Define the Class class
class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    start_time = Column(DateTime, default=datetime.now)
    end_time = Column(DateTime, default=datetime.now)
    teacher = relationship('Teacher', backref='classes')
    student = relationship('Student', backref='classes')

# Create the engine and tables
engine = create_engine('sqlite:///school.db')  # Change the URL to your desired database
Base.metadata.create_all(engine)
