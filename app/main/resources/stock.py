from app.main import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    price = db.Column(db.Float, unique=True, nullable=False)
    update_time = db.Column(db.Date, nullable=True)