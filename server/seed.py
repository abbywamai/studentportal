#!/usr/bin/env python3

from app import app
from models import db, Teacher, Student, Class

with app.app_context():

    Teacher.query.delete()
    Student.query.delete()
    Class.query.delete()

    # Seed data for teachers
    teacher1 = Teacher(
        first_name="John",
        last_name="Doe",
        salary=50000
    )

    teacher2 = Teacher(
        first_name="Jane",
        last_name="Smith",
        salary=60000
    )

    db.session.add_all([teacher1, teacher2])

    # Seed data for students
    student1 = Student(
        first_name="Alice",
        last_name="Johnson",
        gender="Female",
        age=18,
        grade="A"  # Change grade to letter "A"
    )

    student2 = Student(
        first_name="Bob",
        last_name="Smith",
        gender="Male",
        age=17,
        grade="B"  # Change grade to letter "B"
    )

    db.session.add_all([student1, student2])

    # Seed data for classes
    class1 = Class(
        title="Math",
        teacher_id=1,
        student_id=1
    )

    class2 = Class(
        title="Science",
        teacher_id=2,
        student_id=2
    )

    db.session.add_all([class1, class2])

    db.session.commit()
