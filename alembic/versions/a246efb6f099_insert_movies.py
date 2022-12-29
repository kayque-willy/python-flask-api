"""insert movies

Revision ID: a246efb6f099
Revises: 
Create Date: 2022-12-29 13:18:19.154308

"""
from alembic import op
import sqlalchemy as sa
from python_sql_alchemy.repository.filmes_repository import FilmeRepository


# revision identifiers, used by Alembic.
revision = 'a246efb6f099'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    filmes_repository = FilmeRepository()
    filmes_repository.insert("O Senhor dos Anéis - A Sociedade do Anel", "Fantasia", 2001)
    filmes_repository.insert("O Senhor dos Anéis - O Retorno do Rei", "Fantasia", 2003)

def downgrade() -> None:
    filmes_repository = FilmeRepository()
    filmes_repository.delete("O Senhor dos Anéis - A Sociedade do Anel")
    filmes_repository.delete("O Senhor dos Anéis - O Retorno do Rei")
