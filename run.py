from python_sql_alchemy.repository.filmes_repository import FilmeRepository 
from python_sql_alchemy.repository.atores_repository import AtoresRepository

# Repositórios
filmeRepository = FilmeRepository()
atoresRepository = AtoresRepository()

# Insert
filmeRepository.insert("Senhor dos Anéis - as Duas Torres", "Fantasia", 2001)
data = filmeRepository.select_all()
print("\n----------------------Insert----------------------\n")
print(data)

# Update
filmeRepository.update("Senhor dos Anéis - as Duas Torres", "Alta Fantasia", 2002)
data = filmeRepository.select_all()
print("\n----------------------Update----------------------\n")
print(data)

# Delete
filmeRepository.delete("Senhor dos Anéis - as Duas Torres")
data = filmeRepository.select_all()
print("\n----------------------Delete----------------------\n")
print(data)

# Select Join [atores -> filmes]
data = atoresRepository.select_join()
print("\n----------------------Select Join----------------------\n")
print(data)

# Select Join, por relação reversa (collection) [filmes -> atores]
data = filmeRepository.select_all()
filme = data[0]
print("\n----------------------Select Join - relação reversa----------------------\n")
print(filme.titulo, filme.atores)
