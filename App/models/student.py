from App.database import db
from .user import User
from .service_record import ServiceRecord

class Student(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    services = db.relationship('Service', secondary='service_record', backref=db.backref('students', lazy=True))
    accolades = db.relationship('Accolade', secondary='student_accolade', backref=db.backref('students', lazy=True))


    