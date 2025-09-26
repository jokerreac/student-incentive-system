from App.database import db
from .accolade import Accolade
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

    
    def award_accolades(student):
        accolades = Accolade.list()
        total_hours = student.calc_total_hours()
        new_accolades_records = []

        for accolade in accolades:
            if not AccoladeRecord.query.filter_by(student_id=student.id, accolade_id=accolade.id).all() and total_hours >= accolade.target_hours:
               new_accolade_record = AccoladeRecord(student.id, accolade.id)
               db.session.add(new_accolade_record)
               new_accolades_records.append(new_accolade_record)

        if new_accolades_records:        
            db.session.commit()
            return new_accolades_records
