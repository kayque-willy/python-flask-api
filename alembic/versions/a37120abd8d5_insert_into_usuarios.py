"""insert into usuarios

Revision ID: a37120abd8d5
Revises: 9c0056035873
Create Date: 2022-12-29 13:46:32.967432

"""
from alembic import op
import sqlalchemy as sa
from python_sql_alchemy.config.connection import DBConnectionHandler


# revision identifiers, used by Alembic.
revision = 'a37120abd8d5'
down_revision = '9c0056035873'
branch_labels = None
depends_on = None


def upgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    engine.execute(
        """
           INSERT INTO usuario(id, nome, descrição) 
           VALUES 
           (1,'Kayque','Admin'), 
           (2,'Fulano','User');
        """
    )

def downgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    engine.execute(
        """
           DELETE FROM usuario WHERE id = 1;
        """
    )
    engine.execute(
        """
           DELETE FROM usuario WHERE id = 2;
        """
    )