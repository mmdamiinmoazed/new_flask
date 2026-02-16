from . import db , app
from sqlalchemy import Column




class Product (db.Model) : 
    
    __tablename__ = "product"
    _id = db.Column(db.Integer , autoincrement=True , primary_key = True)
    _name = db.Column(db.String , nullable = False)
    _stock = db.Column(db.String , nullable = False)
    _price = db.Column(db.Integer, nullable = False)
    _description = db.Column(db.String , nullable = False)
    _photo = db.Column(db.String , nullable = False)
    _category = db.Column(db.Enum("dessert" , "drink" , "food"))
with app.app_context() : 
    db.create_all()
    