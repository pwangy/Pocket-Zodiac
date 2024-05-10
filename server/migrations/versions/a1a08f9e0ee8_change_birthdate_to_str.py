"""change birthdate to str

Revision ID: a1a08f9e0ee8
Revises: 8c8015bfb66b
Create Date: 2024-05-07 15:40:32.778043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1a08f9e0ee8'
down_revision = '8c8015bfb66b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_zodiacs', schema=None) as batch_op:
        batch_op.alter_column('additional_birthdate',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('birthdate',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('birthdate',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)

    with op.batch_alter_table('user_zodiacs', schema=None) as batch_op:
        batch_op.alter_column('additional_birthdate',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
