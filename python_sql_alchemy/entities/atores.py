from python_sql_alchemy.config.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Atores(Base):
    # Define qual tabela do banco a classe se relaciona
    __tablename__ = "atores"

    # Colunas
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    # Criação de chave estrangeira, a outra maneira de referenciar é por Relationship
    titulo_filme = Column(String, ForeignKey("filmes.titulo"))

    # To string
    def __repr__(self):
        return f"({self.nome}, filme: {self.titulo_filme})"
