import json
from python_sql_alchemy.config.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from python_sql_alchemy.entities.atores import Atores


class Filmes(Base):
    # Define qual tabela do banco a classe se relaciona
    __tablename__ = "filmes"

    # Colunas
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    # Relacionamento bidirecional (collection) com a tabela atores por meio de RelationShip
    atores = relationship("Atores", backref="atores", lazy="subquery")

    # To string
    def __repr__(self):
        return f"({self.titulo}, ano: {self.ano})"