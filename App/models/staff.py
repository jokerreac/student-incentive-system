from App.database import db
from .user import User
from App.utils.display import display_table

class Staff(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    services = db.relationship('Service', secondary='service_record', backref=db.backref('staff', lazy=True))


    def list():
        return Staff.query.all()
        

    def get_by_id(id):
        return Staff.query.get(id)
    

    def process_service_request():
        from .student import Student
        from .service import Service
        from .service_record import ServiceRecord

        print(f"\n======== PROCESS SERVICE REQUEST MENU ========")
        print("\n")

        if not Staff.list_staff():
            return
        print("\n")

        while True:
            staff_id = input("Select Staff ID: ")
            if Staff.query.get(staff_id) is not None:
                print("\n")
                break
            else:
                print("Selection does not exist. Please enter a valid Staff ID.\n")

        if not ServiceRecord.list_pending_filtered(staff_id):
            return
        print("\n")
        





            