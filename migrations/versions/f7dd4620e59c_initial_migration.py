"""initial migration

Revision ID: f7dd4620e59c
Revises: 
Create Date: 2025-06-24 22:10:53.305455

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f7dd4620e59c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('climate', schema=None) as batch_op:
        batch_op.alter_column('winddirection',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.Float(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('climate', schema=None) as batch_op:
        batch_op.alter_column('winddirection',
               existing_type=sa.Float(),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###
