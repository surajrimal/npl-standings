"""Initial migration 2

Revision ID: e371e4019b31
Revises: 387d3e3d7d6d
Create Date: 2024-12-07 15:57:54.718661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e371e4019b31'
down_revision = '387d3e3d7d6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('captain', sa.String(length=100), nullable=False),
    sa.Column('home_ground', sa.String(length=200), nullable=True),
    sa.Column('auction_bid', sa.String(length=100), nullable=True),
    sa.Column('notable_players', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team')
    # ### end Alembic commands ###
