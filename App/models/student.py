from App.database import db
from .user import User

class Student(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    records = db.relationship('ServiceRecord', backref=db.backref('student', lazy=True), foreign_keys='ServiceRecord.student_id')
    accolades = db.relationship('StudentAccolade', backref=db.backref('student', lazy=True), foreign_keys='StudentAccolade.student_id')


    def list():
        return Student.query.all()
        
    
    def get_by_id(id):
        return Student.query.get(id)
    

    def calc_total_hours(self):
        total_hours = 0
        for r in self.records:
            if r.status == "Approved":
                total_hours += int(r.num_hours)
        
        return total_hours


    def list_hours_sorted():
        students = Student.list()
        leaderboard = []
        
        for s in students:
            leaderboard.append({"student" : s, "hours" : s.calc_total_hours()})
        
        return sorted(leaderboard, key=lambda x: x["hours"], reverse=True)