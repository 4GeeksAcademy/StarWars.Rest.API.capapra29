from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class Planeta(db.Model):
    
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    weather = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planeta %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "weather": self.weather
          
        }
    
class Favorito(db.Model):
   

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    person=db.relationship("User")
    planeta_id = db.Column(db.Integer, db.ForeignKey("planeta.id"))
    planeta=db.relationship(Planeta)
    personaje_id = db.Column(db.Integer, db.ForeignKey("personaje.id"))
    personaje=db.relationship("Personaje")

    def __repr__(self):
        return '<Favorito %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "planeta_id": self.planeta_id,
            "personaje_id": self.personaje_id
        
         
        }
    
class Personaje(db.Model):
    
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Personaje %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color
        }

