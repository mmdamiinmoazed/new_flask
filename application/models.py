from . import db , app

class User (db.Model) : 
    __tablename__ = "user"
    _id = db.Column(db.Integer , autoincrement=True , primary_key = True)
    _fullname = db.Column(db.String , nullable = False)
    _username = db.Column(db.String , nullable = False)
    _age = db.Column(db.Integer, nullable = False)
    _password = db.Column(db.String, nullable = False)
    @property
    def fullname() : 
        return User._fullname
    
    @property
    def username() : 
        return User._username

    @property
    def age() : 
        return User._age

    @property
    def password() : 
        return User._password

class Product (db.Model) : 
    __tablename__ = "product"
    _id = db.Column(db.Integer , autoincrement=True , primary_key = True)
    _name = db.Column(db.String , nullable = False)
    _stock = db.Column(db.String , nullable = False)
    _price = db.Column(db.Integer, nullable = False)
    _user_id = db.relationship(db.String , db.ForeignKey("user._id") , )
    user = db.relationship("User", backref=db.backref("products", lazy=True))
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
