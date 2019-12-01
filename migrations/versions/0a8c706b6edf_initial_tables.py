"""Initial Tables

Revision ID: 0a8c706b6edf
Revises: 
Create Date: 2019-12-01 10:01:27.024077

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0a8c706b6edf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.PrimaryKeyConstraint('game_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('playlist',
    sa.Column('playlist_id', sa.Integer(), nullable=False),
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('extreme', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('playlist_id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('playlist_games',
    sa.Column('playlist_id', sa.Integer(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.game_id'], ),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlist.playlist_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playlist_games')
    op.drop_table('playlist')
    op.drop_table('user')
    op.drop_table('game')
    # ### end Alembic commands ###