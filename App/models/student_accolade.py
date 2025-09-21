from App.database import db
from datetime import date

class StudentAccolade(db.Model):
    __tablename__='student_accolade'
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    accolade_id = db.Column(db.Integer, db.ForeignKey('accolade.id'), primary_key=True)
    date_earned = db.Column(db.Date, nullable=False)


    def __init__(self, student_id, accolade_id):
        self.student_id = student_id
        self.accolade_id = accolade_id
        self.date_earned = date.today()
    

    def list():
        return StudentAccolade.query.all()

    
    def award_accolades(student, total_hours):
        from .accolade import Accolade

        accolades = Accolade.list()
        student_name = f"{student.first_name} {student.last_name}"

        for accolade in accolades:
            if not StudentAccolade.query.filter_by(student_id=student.id, accolade_id=accolade.id).all() and total_hours >= accolade.target_hours:
               db.session.add(StudentAccolade(student.id, accolade.id))
               print(f"[Accolade Unlocked] {student_name} just earned {accolade.title} - {accolade.target_hours} hours of service!")

        db.session.commit()