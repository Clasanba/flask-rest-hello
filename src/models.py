from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            # do not serialize the password, its a security breach
        }
        
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(80), unique=False, nullable=False)
    species = db.Column(db.Boolean(), unique=False, nullable=False)
    gender = db.Column(db.Boolean(), unique=False, nullable=False)
    type = db.Column(db.String(120), unique=False, nullable=False)
    image = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(120), unique=False, nullable=False)
    created = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "gender": self.gender,
            "type": self.type,
            "image": self.image,
            "url": self.url,
            "created": self.created,
        }
        
class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(80), unique=False, nullable=False)
    dimension = db.Column(db.Boolean(), unique=False, nullable=False)
    url = db.Column(db.String(120), unique=False, nullable=False)
    created = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Locations %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "dimension": self.dimension,
            "url": self.url,
            "created": self.created,
        }
        
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characters = db.Column(db.String(120), db.ForeignKey('characters.id'),unique=True, nullable=False)
    locations = db.Column(db.String(80), db.ForeignKey('locations.id'), unique=False, nullable=False)
    user_id = db.Column(db.Boolean(), db.ForeignKey('user.id'), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "characters": self.characters,
            "locations": self.locations,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }