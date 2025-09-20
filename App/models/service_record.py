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
    
    
    def create_service_record(student_id, staff_id, service_id, num_hours):
        db.session.add(ServiceRecord(student_id, staff_id, service_id, num_hours))
        db.session.commit()
        print("Service Record Created!")


    """def list_pending_filtered(staff_id):
        from .staff import Staff
        from .student import Student
        from .service import Service

        staff_name = f"{Staff.query.get(staff_id).first_name} {Staff.query.get(staff_id).last_name}"
        print(f"Service Requests Awaiting Approval - [{staff_name}]\n")
        print(f"{'Record ID':<15} {'Student':<20} {'Service':<30} {'Hours':<10} {'Request Date':<16} {'Status':<16}")
        print("-" * 105)

        service_requests = ServiceRecord.query.filter_by(staff_id=staff_id, status="Pending").all()
        if not service_requests:
            return False

        for r in service_requests:
            student_name = f"{Student.query.get(r.student_id).first_name} {Student.query.get(r.student_id).last_name}"
            service_name = f"{Service.query.get(r.service_id).name}"
            request_date = r.request_date.strftime('%Y-%m-%d')

            print(f"{r.id:<15} {student_name:<20} {service_name:<30} {r.num_hours:<10} {request_date:<16} {r.status:<16}")
        return True"""
