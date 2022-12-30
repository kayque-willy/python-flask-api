from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer

# Arquivo de exemplificação de todo funcionamento do SQLAlchemy
# ----------------------------- Configurações -----------------------------
dialect = 'mysql+pymysql' + '://'
user = 'root' + ':'
password = '' + '@'
bd = 'localhost' + ':'
port = '3306'  + '/'
name = 'cinema'

# ----------------------------- Criação da Engine -----------------------------
# engine = create_engine('mysql+pymysql://root:@localhost:3306/cinema')
engine = create_engine(dialect + user + password + bd + port + name)

# ----------------------------- Criação da base declarativa -----------------------------
Base = declarative_base()

# ----------------------------- Criação da sessão -----------------------------
Session = sessionmaker(bind=engine)
session = Session()

# ----------------------------- Entidades -----------------------------

class Filmes(Base):
    # Define qual tabela do banco a classe se relaciona
    __tablename__ = "filmes"

    # Colunas
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"({self.titulo}, ano: {self.ano})"

# ----------------------------- SQL -----------------------------
# Insert
new_filme = Filmes(titulo='Dracula', genero='Ação', ano=2001)
session.add(new_filme)
session.commit()

# Delete
session.query(Filmes).filter(Filmes.titulo=='Dracula').delete()
session.commit()

# Update 
session.query(Filmes).filter(Filmes.titulo=='Senhor dos anéis').update({"ano" : 2003})
session.commit()

# Select
filme = session.query(Filmes).all()
print(filme)

session.close()