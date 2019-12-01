from sqlalchemy.dialects.postgresql import UUID
from fp_api.extensions import db

playlist_games = db.Table('playlist_games',
  db.Column('playlist_id', db.ForeignKey('playlist.playlist_id')),
  db.Column('game_id', db.ForeignKey('game.game_id')))