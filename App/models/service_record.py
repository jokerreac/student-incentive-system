from App.database import db
from App.utils.display import display_table
from datetime import date

class ServiceRecord(db.Model):
    __tablename__='service_record'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    num_hours = db.Column(db.Integer, nullable=False)
    request_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    processed_date = db.Column(db.Date, nullable=True)


    def __init__(self, student_id, staff_id, service_id, num_hours):
        self.student_id = student_id
        self.staff_id = staff_id
        self.service_id = service_id
        self.num_hours = num_hours
        self.request_date = date.today()
        self.status = "Pending"
        self.processed_date = None


    def list():
        return ServiceRecord.query.all()
    
    
    def get_by_id(id):
        return ServiceRecord.query.get(id)


    def create_service_record(student_id, staff_id, service_id, num_hours):
        db.session.add(ServiceRecord(student_id, staff_id, service_id, num_hours))
        db.session.commit()


    def process_service_request(service_record, action):
        service_record.status = action
        service_record.processed_date = date.today()
        db.session.add(service_record)
        db.session.commit()

    
    def list_pending_by_staff_id(id):
        return ServiceRecord.query.filter_by(staff_id=id, status="Pending").all()
    


