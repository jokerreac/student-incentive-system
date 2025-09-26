from App.database import db
from datetime import date

class AccoladeRecord(db.Model):
    __tablename__='accolade_record'
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    accolade_id = db.Column(db.Integer, db.ForeignKey('accolade.id'), primary_key=True)
    date_earned = db.Column(db.Date, nullable=False)


    def __init__(self, student_id, accolade_id):
        self.student_id = student_id
        self.accolade_id = accolade_id
        self.date_earned = date.today()
    

    def list():
        return AccoladeRecord.query.all()
    

    def get_by_id(student_id, accolade_id):
        return AccoladeRecord.query.get((student_id, accolade_id))