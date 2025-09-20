from App.database import db

class StudentAccolade(db.Model):
    __tablename__='student_accolade'
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    accolade_id = db.Column(db.Integer, db.ForeignKey('accolade.id'), primary_key=True)
    date_earned = db.Column(db.Date, nullable=False)


    def __init__(self, student_id, accolade_id, date_earned):
        self.student_id = student_id
        self.accolade_id = accolade_id
        self.date_earned = date_earned
    

    def list():
        return StudentAccolade.query.all()
        