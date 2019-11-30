from fp_api.extensions import db

class Game(db.Model):
  game_id = db.Column(db.Integer, primary_key=True)
  uuid =    db.Column(db.String(36), nullable=False)