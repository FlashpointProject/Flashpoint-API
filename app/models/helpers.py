from sqlalchemy.dialects.postgresql import UUID
from app.extensions import db

playlist_games = db.Table('playlist_games',
  db.Column('playlist_uuid', UUID(as_uuid=True)),
  db.Column('game_uuid', UUID(as_uuid=True)))