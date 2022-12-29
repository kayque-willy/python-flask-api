"""create table usuario

Revision ID: 9c0056035873
Revises: a246efb6f099
Create Date: 2022-12-29 13:19:42.844285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c0056035873'
down_revision = 'a246efb6f099'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'usuario',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(50), nullable=False),
        sa.Column('descrição', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('usuario')
