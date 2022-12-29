from python_sql_alchemy.config.connection import DBConnectionHandler
from python_sql_alchemy.entities.filmes import Filmes
from python_sql_alchemy.entities.atores import Atores
from sqlalchemy.orm.exc import NoResultFound


class   AtoresRepository:

    # Select
    def select_join(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(
                    Atores, 
                    Filmes
                ).join(
                    Filmes, Atores.titulo_filme==Filmes.titulo
                ).with_entities(
                    Atores.nome,
                    Filmes.titulo,
                    Filmes.genero
                ).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    # Insert
    # def insert(self, titulo, genero, ano):
    #     with DBConnectionHandler() as db:
    #         data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
    #         db.session.add(data_insert)
    #         db.session.commit()

    # def delete(self, titulo):
    #     with DBConnectionHandler() as db:
    #         db.session.query(Filmes).filter(Filmes.titulo==titulo).delete()
    #         db.session.commit()

    # def update(self, titulo, genero, ano):
    #     with DBConnectionHandler() as db:
    #         db.session.query(Filmes).filter(Filmes.titulo==titulo).update({
    #             "ano" : ano, 
    #             "genero":genero
    #         })
    #         db.session.commit()