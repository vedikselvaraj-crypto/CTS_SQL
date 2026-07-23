"""
================================================================================
COURSE SERVICE ORM MODELS (models.py)
================================================================================
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    credits = db.Column(db.Integer, default=3)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits
        }
