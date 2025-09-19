from App.database import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


    def __init__(self, id, name):
        self.id = id
        self.name = name

    