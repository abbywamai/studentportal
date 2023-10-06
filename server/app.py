from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime
from models import db , User, Student, Teacher,  Grade
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a strong secret key
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key_here'  # Change this to a strong JWT secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)  # JWT token expiration time


db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)
migrate = Migrate(app, db)


# Define a resource for teacher signup
class TeacherSignupResource(Resource):
    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {'message': 'Username and password are required'}, 400

        existing_teacher = Teacher.query.filter_by(username=username).first()
        if existing_teacher:
            return {'message': 'Username already exists'}, 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_teacher = Teacher(username=username, password=hashed_password)
        db.session.add(new_teacher)
        db.session.commit()

        return {'message': 'Teacher registration successful'}, 201

# Define a resource for teacher login
class TeacherLoginResource(Resource):
    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {'message': 'Username and password are required'}, 400

        teacher = Teacher.query.filter_by(username=username).first()

        if not teacher or not bcrypt.check_password_hash(teacher.password, password):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=teacher.id)
        return {'access_token': access_token}, 200
# Define a resource for student signup
class StudentSignupResource(Resource):
    def post(self):
        data = request.get_json()

        student_id = data.get('student_id')
        username = data.get('username')
        password = data.get('password')

        if not student_id or not username or not password:
            return {'message': 'Student ID, username, and password are required'}, 400

        existing_student = Student.query.filter_by(student_id=student_id).first()
        if existing_student:
            return {'message': 'Student ID already exists'}, 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_student = Student(student_id=student_id, username=username, password=hashed_password)
        db.session.add(new_student)
        db.session.commit()

        return {'message': 'Student registration successful'}, 201

# Define a resource for student login
class StudentLoginResource(Resource):
    def post(self):
        data = request.get_json()

        student_id = data.get('student_id')
        password = data.get('password')

        if not student_id or not password:
            return {'message': 'Student ID and password are required'}, 400

        student = Student.query.filter_by(student_id=student_id).first()

        if not student or not bcrypt.check_password_hash(student.password, password):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=student.id)
        return {'access_token': access_token}, 200

# Define a resource for viewing student grades
class StudentGradesResource(Resource):
    @jwt_required()
    def get(self):
        current_student_id = get_jwt_identity()
        student = Student.query.get(current_student_id)

        if not student:
            return {'message': 'Student not found'}, 404

        # Retrieve the student's grades
        grades = Grade.query.filter_by(student_id=current_student_id).all()

        grade_data = []
        for grade in grades:
            grade_data.append({
                'grade_value': grade.grade_value,
                'date_submitted': grade.date_submitted.strftime('%Y-%m-%d')
            })

        return {'grades': grade_data}, 200

# Define a resource for posting student grades (teacher role)
class PostStudentGradesResource(Resource):
    @jwt_required()
    def post(self):
        current_teacher_id = get_jwt_identity()

        data = request.get_json()

        student_id = data.get('student_id')
        course_id = data.get('course_id')
        grade_value = data.get('grade_value')
        date_submitted = datetime.datetime.now()

        # Check if the teacher is authorized to post grades for the given course

        # Check if the student exists
        student = Student.query.filter_by(id=student_id).first()
        if not student:
            return {'message': 'Student not found'}, 404

        # Create a new grade entry
        new_grade = Grade(
            student_id=student_id,
            course_id=course_id,
            grade_value=grade_value,
            date_submitted=date_submitted
        )

        db.session.add(new_grade)
        db.session.commit()

        return {'message': 'Grade posted successfully'}, 201

# Add these resources to the API
api.add_resource(StudentSignupResource, '/student/signup')
api.add_resource(StudentLoginResource, '/student/login')
api.add_resource(StudentGradesResource, '/student/grades')
api.add_resource(PostStudentGradesResource, '/teacher/postgrades')

# Define similar resources for teacher and other routes as needed

# Add these resources to the API
api.add_resource(TeacherSignupResource, '/teacher/signup')
api.add_resource(TeacherLoginResource, '/teacher/login')

# Define similar resources for student signup and login


if __name__ == '__main__':
    app.run(debug=True)
