from App.database import db
from App.utils.display import display_table

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


    def __init__(self, name):
        self.name = name


    def list():
        return Service.query.all()
        

    def get_by_id(id):
        return Service.query.get(id)

    