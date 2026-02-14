from . import db , app

class Product (db.Model) : 
    __tablename__ = "product"
    _id = db.Column(db.Integer , autoincrement=True , primary_key = True)
    _name = db.Column(db.String , nullable = False)
    _stock = db.Column(db.String , nullable = False)
    _price = db.Column(db.Integer, nullable = False)
    @property
    def name() : 
        return Product._name
    @property
    def stock() : 
        return Product._stock
    @property
    def price() : 
        return Product._price
with app.app_context() : 
    db.create_all()
    print("database and columns of it got created")
