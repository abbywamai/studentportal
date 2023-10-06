from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import  db, User, Teacher, Student, Grade
from app import app



# Create an application context
with app.app_context():
    # Create users
    user1 = User(username='teacher1', password='password1', is_teacher=True)
    user2 = User(username='teacher2', password='password2', is_teacher=True)
    user3 = User(username='student1', password='password3', is_teacher=False)
    user4 = User(username='student2', password='password4', is_teacher=False)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)

    # Create teachers
    teacher1 = Teacher(teacher_id=1001, hire_date=datetime(2022, 1, 15), user=user1)
    teacher2 = Teacher(teacher_id=1002, hire_date=datetime(2022, 3, 20), user=user2)

    db.session.add(teacher1)
    db.session.add(teacher2)

    # Create students
    student1 = Student(student_id=2001, enrollment_date=datetime(2022, 2, 5), user=user3)
    student2 = Student(student_id=2002, enrollment_date=datetime(2022, 4, 10), user=user4)

    db.session.add(student1)
    db.session.add(student2)

    # Create grades
    grade1 = Grade(grade_value='A', date_submitted=datetime(2022, 3, 1), student=student1)
    grade2 = Grade(grade_value='B', date_submitted=datetime(2022, 3, 15), student=student1)
    grade3 = Grade(grade_value='A', date_submitted=datetime(2022, 4, 1), student=student2)
    grade4 = Grade(grade_value='C', date_submitted=datetime(2022, 4, 15), student=student2)

    db.session.add(grade1)
    db.session.add(grade2)
    db.session.add(grade3)
    db.session.add(grade4)

    # Commit the changes to the database
    db.session.commit()
