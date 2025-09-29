from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)


    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.set_password(password)
    

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    

    def list(): 
        return User.query.all()


    def get_name(self):
        return f"{self.first_name} {self.last_name}"
    

    def get_leaderboard():
        from .student import Student        
        students = Student.list()
        leaderboard = []
        
        for s in students:
            leaderboard.append({"student" : s, "hours" : s.calc_total_hours()})
        
        return sorted(leaderboard, key=lambda x: x["hours"], reverse=True)
        


