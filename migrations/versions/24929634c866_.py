"""empty message

Revision ID: 24929634c866
Revises: a5cffa318ac2
Create Date: 2024-11-20 23:47:49.581019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24929634c866'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planeta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('weather', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planeta')
    # ### end Alembic commands ###
