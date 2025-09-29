from App.database import db
from .user import User
from .service_record import ServiceRecord
from .accolade import Accolade
from .accolade_record import AccoladeRecord

class Student(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    records = db.relationship('ServiceRecord', backref=db.backref('student', lazy=True), foreign_keys='ServiceRecord.student_id')
    accolades = db.relationship('AccoladeRecord', backref=db.backref('student', lazy=True), foreign_keys='AccoladeRecord.student_id')


    def list():
        return Student.query.all()
        
    
    def get_by_id(id):
        return Student.query.get(id)
    

    def request_service_log(self, staff_id, service_id, num_hours):
        service_record = ServiceRecord(self.id, staff_id, service_id, num_hours)
        self.records.append(service_record)
        db.session.commit()
        return service_record
    

    def award_accolades(self):
        accolades = Accolade.list()
        total_hours = self.calc_total_hours()
        new_accolade_records = []

        for accolade in accolades:
            if not AccoladeRecord.get_by_id(self.id, accolade.id) and total_hours >= accolade.target_hours:
               new_accolade_record = AccoladeRecord(self.id, accolade.id)
               self.accolades.append(new_accolade_record)
               new_accolade_records.append(new_accolade_record)

        if new_accolade_records:        
            db.session.commit()

        return new_accolade_records
        
    
    def get_accolades(self):
        return self.accolades
    

    def calc_total_hours(self):
        total_hours = 0
        for r in self.records:
            if r.status == "Approved":
                total_hours += int(r.num_hours)
        
        return total_hours