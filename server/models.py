from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_teacher = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password, is_teacher):
        self.username = username
        self.password = password
        self.is_teacher = is_teacher

class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, unique=True, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=backref('teacher', uselist=False))

    def __init__(self, teacher_id, hire_date, user):
        self.teacher_id = teacher_id
        self.hire_date = hire_date
        self.user = user

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, unique=True, nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=backref('student', uselist=False))

    def __init__(self, student_id, enrollment_date, user):
        self.student_id = student_id
        self.enrollment_date = enrollment_date
        self.user = user
"ASDSD"
class Grade(db.Model):
    __tablename__ = 'grade'

    id = db.Column(db.Integer, primary_key=True)
    grade_value = db.Column(db.String(2), nullable=False)
    date_submitted = db.Column(db.Date, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    student = db.relationship('Student', backref=backref('grades', lazy='dynamic'))

    def __init__(self, grade_value, date_submitted, student):
        self.grade_value = grade_value
        self.date_submitted = date_submitted
        self.student = student
