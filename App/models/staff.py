from App.database import db
from .user import User
from .service_record import ServiceRecord
from datetime import date

class Staff(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    records = db.relationship('ServiceRecord', backref=db.backref('staff', lazy=True), foreign_keys='ServiceRecord.staff_id')


    def list():
        return Staff.query.all()
        

    def get_by_id(id):
        return Staff.query.get(id)
    

    def log_service_hours(self, student_id, service_id, num_hours):
        service_record = ServiceRecord(student_id, self.id, service_id, num_hours, "Approved")
        self.records.append(service_record)
        db.session.commit()
        return service_record
    

    def process_service_request(self, service_record, action):
        service_record.status = action
        service_record.processed_date = date.today()
        db.session.commit()
        return service_record




            