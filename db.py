from flask_sqlalchemy import SQLAlchemy
from app.models.student import Student
from app.models.teacher import Teacher
from app.models.course import Course

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
#hey collins sorry for disturbing. i miss you 
