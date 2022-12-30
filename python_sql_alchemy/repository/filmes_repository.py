from python_sql_alchemy.config.connection import DBConnectionHandler
from python_sql_alchemy.entities.filmes import Filmes
from sqlalchemy.orm.exc import NoResultFound


class FilmeRepository:

    # Insert
    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            try:
                data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    # Select
    def select_all(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    # Select by title
    def select_by_title(self, titulo):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).filter(Filmes.titulo == titulo).one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    # Update
    def update(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).update(
                    {"ano": ano, "genero": genero}
                )
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    # Delete
    def delete(self, titulo):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
