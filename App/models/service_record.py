from App.database import db

class ServiceRecord(db.Model):
    __tablename__='service_record'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    num_hours = db.Column(db.Integer, nullable=False)
    request_date = db.Column(db.Date, nullable=False)
    processed_date = db.Column(db.Date, nullable=True)

    def __init__(self, id, student_id, staff_id, service_id, num_hours, request_date):
        self.id = id
        self.student_id = student_id
        self.staff_id = staff_id
        self.service_id = service_id
        self.num_hours = num_hours
        self.request_date = request_date

