from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()

# Define the Teacher class
class Teacher(db.Model, SerializerMixin):
    __tablename__ = 'teachers'

    serialize_rules = ('-teacher_classes.teacher',)


    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    salary = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    teacher_classes = db.relationship('Class', backref='teacher')

# Define the Student class
class Student(db.Model, SerializerMixin):
    __tablename__ = 'students'

    serialize_rules = ('-student_classes.student',)

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    stud_classes = db.relationship('Class', backref='student')

# Define the Class class
class Class(db.Model, SerializerMixin):
    __tablename__ = 'classes'

    serialize_rules = ('-teacher.teacher_classes', '-student.stud_classes',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, default=datetime.now)


