from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    grade = db.Column(db.String(2), nullable=True)

    def __repr__(self):
        return f"{self.student.name} - {self.course.name}"
