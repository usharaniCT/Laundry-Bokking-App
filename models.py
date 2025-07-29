from app import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    room_no = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    cloth_type = db.Column(db.String(100), nullable=False)
    wash_type = db.Column(db.String(100), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    clothes = db.Column(db.String(100))
    status = db.Column(db.String(50), default='Pending')
    payment_status = db.Column(db.String(50), default='Unpaid')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
