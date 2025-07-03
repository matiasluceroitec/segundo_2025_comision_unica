from app import db

from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    is_active = db.Column(db.Boolean, default=True) 
    climates = db.relationship(
        'Climate',
        backref='user',
        lazy=True
    )


    def __str__(self):
        return self.username

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    climates = db.relationship(
        'Climate',
        backref='city',
        lazy=True
    )

    def __str__(self):
        return self.name


class Climate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    ciudad_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    windspeed = db.Column(db.Float, nullable=True)
    winddirection = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __str__(self) -> str:
        return f"{self.date} {self.ciudad_id} {self.temperature}"
