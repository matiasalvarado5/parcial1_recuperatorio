from dataclasses import dataclass
from app import db
from app.audit import AuditMixin, SoftDeleteMixin

@dataclass(init=False, repr=True, eq=True)
class UserData(SoftDeleteMixin, db.Model):
    __tablename__ = 'users_data'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(80), nullable=False)
    lastname: str = db.Column(db.String(80), nullable=False)
    phone: str = db.Column(db.String(120), nullable=False)
    address: str = db.Column(db.String(120), nullable=False)
    city: str   = db.Column(db.String(120), nullable=False)
    country: str = db.Column(db.String(120), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    #Relacion Uno a Uno bidireccional con User
    #Flask Web Development Capitulo: Database Relationships Revisited Pag 49,149 
    user = db.relationship("User", back_populates='data', uselist=False)
    
    #Relacion Muchos a Uno bidireccional con Profile
    profile_id = db.Column('profile_id', db.Integer, db.ForeignKey('profiles.id'))
    profile = db.relationship("Profile", back_populates='data')

    def __init__(self, firstname: str = None, lastname: str = None, phone: str = None, address: str = None, city: str = None, country: str = None, profile = None):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.address = address
        self.city = city
        self.country = country
        self.profile = profile
