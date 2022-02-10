"""adicionada coluna obs na tabela tb_products

Revision ID: 3b6922defe75
Revises: da990bf62625
Create Date: 2022-02-07 21:17:05.031033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b6922defe75'
down_revision = 'da990bf62625'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('tb_products', sa.Column('obs', sa.String(200)))


def downgrade():
    op.drop_column('tb_products', 'obs')
