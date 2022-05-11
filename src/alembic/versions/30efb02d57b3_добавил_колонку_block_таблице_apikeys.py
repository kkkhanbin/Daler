"""Добавил колонку block таблице apikeys

Revision ID: 30efb02d57b3
Revises: c30c9868dbbb
Create Date: 2022-04-16 22:17:27.248628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30efb02d57b3'
down_revision = 'c30c9868dbbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('apikeys', sa.Column('block', sa.Boolean(), server_default='False', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('apikeys', 'block')
    # ### end Alembic commands ###
