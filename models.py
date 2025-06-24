from app import db


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

    def __str__(self) -> str:
        return f"{self.date} {self.ciudad_id} {self.temperature}"
