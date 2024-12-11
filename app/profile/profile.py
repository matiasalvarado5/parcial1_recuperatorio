from dataclasses import dataclass
from app import db
from app.audit import AuditMixin, SoftDeleteMixin

@dataclass(init=False, repr=True, eq=True)
class Profile(SoftDeleteMixin, AuditMixin, db.Model):
    __tablename__ = 'profiles'
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), nullable=False)
    #Relación Uno a Muchos bidireccional con UserData
    data = db.relationship('UserData', back_populates='profile')

