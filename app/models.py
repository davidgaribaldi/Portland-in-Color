from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(75))
    medium = db.Column(db.String(20), index=True)
    portrait = db.Column(db.String(12), nullable=True)

