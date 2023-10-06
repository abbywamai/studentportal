from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_migrate import Migrate
from datetime import datetime
from models import db, Teacher, Student, Class  # Import your models here

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatwave.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app,db)

db.init_app(app)
api = Api(app)


class TeacherResource(Resource):
    def get(self):
        teachers = [teacher.to_dict() for teacher in Teacher.query.all()]
        return make_response(jsonify(teachers), 200)

    def post(self):
        data = request.json
        new_teacher = Teacher(
            first_name=data['first_name'],
            last_name=data['last_name'],
            salary=data['salary']
        )
        db.session.add(new_teacher)
        db.session.commit()
        teacher_dict = new_teacher.to_dict()
        return make_response(jsonify(teacher_dict), 201)

class StudentResource(Resource):
    def get(self):
        students = [student.to_dict() for student in Student.query.all()]
        return make_response(jsonify(students), 200)

    def post(self):
        data = request.json
        new_student = Student(
            first_name=data['first_name'],
            last_name=data['last_name'],
            gender=data['gender'],
            age=data['age'],
            grade=data['grade']
        )
        db.session.add(new_student)
        db.session.commit()
        student_dict = new_student.to_dict()
        return make_response(jsonify(student_dict), 201)

class ClassResource(Resource):
    def get(self):
        classes = [class_obj.to_dict() for class_obj in Class.query.all()]
        return make_response(jsonify(classes), 200)

    def post(self):
        data = request.json
        new_class = Class(
            title=data['title'],
            teacher_id=data['teacher_id'],
            student_id=data['student_id'],
            start_time=datetime.now(),
            end_time=datetime.now()
        )
        db.session.add(new_class)
        db.session.commit()
        class_dict = new_class.to_dict()
        return make_response(jsonify(class_dict), 201)
    
class TeacherByIdResource(Resource):
    def get(self, id):
        teacher = Teacher.query.filter_by(id=id).first()
        if teacher:
            teacher_dict = teacher.to_dict()
            return make_response(jsonify(teacher_dict), 200)
        else:
            return make_response(jsonify({'message': 'Teacher not found'}), 404)

    def put(self, id):
        teacher = Teacher.query.filter_by(id=id).first()
        if teacher:
            data = request.json
            teacher.first_name = data.get('first_name', teacher.first_name)
            teacher.last_name = data.get('last_name', teacher.last_name)
            teacher.salary = data.get('salary', teacher.salary)
            db.session.commit()
            teacher_dict = teacher.to_dict()
            return make_response(jsonify(teacher_dict), 200)
        else:
            return make_response(jsonify({'message': 'Teacher not found'}), 404)

    def delete(self, id):
        teacher = Teacher.query.filter_by(id=id).first()
        if teacher:
            db.session.delete(teacher)
            db.session.commit()
            return make_response(jsonify({'message': 'Teacher deleted'}), 200)
        else:
            return make_response(jsonify({'message': 'Teacher not found'}), 404)

class StudentByIdResource(Resource):
    def get(self, id):
        student = Student.query.filter_by(id=id).first()
        if student:
            student_dict = student.to_dict()
            return make_response(jsonify(student_dict), 200)
        else:
            return make_response(jsonify({'message': 'Student not found'}), 404)

    def put(self, id):
        student = Student.query.filter_by(id=id).first()
        if student:
            data = request.json
            student.first_name = data.get('first_name', student.first_name)
            student.last_name = data.get('last_name', student.last_name)
            student.gender = data.get('gender', student.gender)
            student.age = data.get('age', student.age)
            student.grade = data.get('grade', student.grade)
            db.session.commit()
            student_dict = student.to_dict()
            return make_response(jsonify(student_dict), 200)
        else:
            return make_response(jsonify({'message': 'Student not found'}), 404)

    def delete(self, id):
        student = Student.query.filter_by(id=id).first()
        if student:
            db.session.delete(student)
            db.session.commit()
            return make_response(jsonify({'message': 'Student deleted'}), 200)
        else:
            return make_response(jsonify({'message': 'Student not found'}), 404)

class ClassByIdResource(Resource):
    def get(self, id):
        class_obj = Class.query.filter_by(id=id).first()
        if class_obj:
            class_dict = class_obj.to_dict()
            return make_response(jsonify(class_dict), 200)
        else:
            return make_response(jsonify({'message': 'Class not found'}), 404)

    def put(self, id):
        class_obj = Class.query.filter_by(id=id).first()
        if class_obj:
            data = request.json
            class_obj.title = data.get('title', class_obj.title)
            class_obj.teacher_id = data.get('teacher_id', class_obj.teacher_id)
            class_obj.student_id = data.get('student_id', class_obj.student_id)
            db.session.commit()
            class_dict = class_obj.to_dict()
            return make_response(jsonify(class_dict), 200)
        else:
            return make_response(jsonify({'message': 'Class not found'}), 404)

    def delete(self, id):
        class_obj = Class.query.filter_by(id=id).first()
        if class_obj:
            db.session.delete(class_obj)
            db.session.commit()
            return make_response(jsonify({'message': 'Class deleted'}), 200)
        else:
            return make_response(jsonify({'message': 'Class not found'}), 404)
    

api.add_resource(TeacherResource, '/teachers')
api.add_resource(StudentResource, '/students')
api.add_resource(ClassResource, '/classes')
api.add_resource(TeacherByIdResource, '/teachers/<int:id>')
api.add_resource(StudentByIdResource, '/students/<int:id>')
api.add_resource(ClassByIdResource, '/classes/<int:id>')


if __name__ == '__main__':
    app.run()