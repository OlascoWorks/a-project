from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Site(db.Model):
    name = db.Column(db.String(20), primary_key=True)
    visits = db.Column(db.Integer)
    unique_visits = db.Column(db.Integer)
    
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10))
    tracking_id = db.Column(db.Integer, unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    pck_name = db.Column(db.String(100))
    pck_address = db.Column(db.String(100))
    pck_number = db.Column(db.String(100))
    rcp_name = db.Column(db.String(100))
    rcp_address = db.Column(db.String(100))
    rcp_number = db.Column(db.String(100))
    method = db.Column(db.String(100))
    item_no = db.Column(db.String(10))
    weight = db.Column(db.String(100), default=None)
    extra = db.Column(db.String(100))
    description = db.Column(db.String(100), default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(20))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    is_subscriber = db.Column(db.Boolean, default=False)
    orders = db.relationship('Orders')