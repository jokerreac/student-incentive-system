from App.database import db
from .user import User

class Staff(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    records = db.relationship('ServiceRecord', backref=db.backref('staff', lazy=True), foreign_keys='ServiceRecord.staff_id')


    def list():
        return Staff.query.all()
        

    def get_by_id(id):
        return Staff.query.get(id)
        





            