"""criada tabela tb_products

Revision ID: da990bf62625
Revises: 
Create Date: 2022-02-07 21:03:47.372643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da990bf62625'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tb_products',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('price', sa.Float, nullable=False)
    )


def downgrade():
    op.drop_table('tb_products')
