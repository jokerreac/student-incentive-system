from App.database import db
from .user import User

class Staff(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    services = db.relationship('Service', secondary='service_record', backref=db.backref('staff', lazy=True))