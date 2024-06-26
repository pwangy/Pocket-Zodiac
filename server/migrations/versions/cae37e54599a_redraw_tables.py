"""redraw tables

Revision ID: cae37e54599a
Revises: 
Create Date: 2024-04-30 21:16:46.343111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cae37e54599a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('elements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('qualities', sa.String(), nullable=True),
    sa.Column('desc', sa.String(), nullable=True),
    sa.Column('season', sa.String(), nullable=True),
    sa.Column('direction', sa.String(), nullable=True),
    sa.Column('planet', sa.String(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('smell', sa.String(), nullable=True),
    sa.Column('taste', sa.String(), nullable=True),
    sa.Column('organ', sa.String(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('west',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('gloss', sa.String(), nullable=True),
    sa.Column('desc', sa.String(), nullable=True),
    sa.Column('qualities', sa.String(), nullable=True),
    sa.Column('element', sa.String(), nullable=True),
    sa.Column('modality', sa.String(), nullable=True),
    sa.Column('planet', sa.String(), nullable=True),
    sa.Column('house', sa.Integer(), nullable=True),
    sa.Column('symbol', sa.String(), nullable=True),
    sa.Column('img', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('east',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('qualities', sa.String(), nullable=True),
    sa.Column('desc', sa.String(), nullable=True),
    sa.Column('polarity', sa.String(), nullable=True),
    sa.Column('order_12', sa.Integer(), nullable=True),
    sa.Column('order_60', sa.Integer(), nullable=True),
    sa.Column('western_counterpart', sa.String(), nullable=True),
    sa.Column('element_id', sa.Integer(), nullable=True),
    sa.Column('img', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['element_id'], ['elements.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_zodiacs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('west_id', sa.Integer(), nullable=True),
    sa.Column('east_id', sa.Integer(), nullable=True),
    sa.Column('east_west', sa.String(), nullable=True),
    sa.Column('additional_birthdate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['east_id'], ['east.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['west_id'], ['west.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_zodiacs')
    op.drop_table('east')
    op.drop_table('west')
    op.drop_table('users')
    op.drop_table('elements')
    # ### end Alembic commands ###
