from app.extensions import db

class Game(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  uuid = db.Column(db.String(36), nullable=False)