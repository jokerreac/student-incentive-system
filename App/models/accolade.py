from App.database import db

class Accolade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    target_hours = db.Column(db.Integer, unique=True, nullable=False)


    def __init__(self, title, description, target_hours):
        self.title = title
        self.description = description
        self.target_hours = target_hours


    def list():
        return Accolade.query.all()
        