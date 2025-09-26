from App.database import db
from datetime import date
from sqlalchemy import Enum

class ServiceRecord(db.Model):
    __tablename__='service_record'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    num_hours = db.Column(db.Integer, nullable=False)
    request_date = db.Column(db.Date, nullable=False)
    status = db.Column(Enum("Pending", "Approved", "Denied", name="status_enum"), default="Pending", nullable=False)
    processed_date = db.Column(db.Date, nullable=True)


    def __init__(self, student_id, staff_id, service_id, num_hours, status="Pending"):
        self.student_id = student_id
        self.staff_id = staff_id
        self.service_id = service_id
        self.num_hours = num_hours
        self.request_date = date.today()
        self.status = status

        if status == "Approved":
            self.processed_date = date.today()
        else:
            self.processed_date = None

    def list():
        return ServiceRecord.query.all()
    
    
    def get_by_id(id):
        return ServiceRecord.query.get(id)

    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


    def process_service_request(self, action):
        self.status = action
        self.processed_date = date.today()
        self.save()
        return self

    
    def list_pending_by_staff_id(id):
        return ServiceRecord.query.filter_by(staff_id=id, status="Pending").all()