from . import db

class Property(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(600))
    description = db.Column(db.String(800))
    rooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    property_type = db.Column(db.String(900))
    location = db.Column(db.String(200))
    photo_name = db.Column(db.String(50))

    def __init__(self, title, description, rooms, bathrooms, price, property_type, location, photo_name):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.photo_name = photo_name
    
    def __repr__(self):
        return '<Property %r>' % self.photo_name