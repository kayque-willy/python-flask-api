from flask import make_response, jsonify
from python_sql_alchemy.repository.filmes_repository import FilmeRepository


class FilmeController:
    filme_repository = FilmeRepository()

    def get_all_filmes(self):
        data = self.filme_repository.select_all()
        filmes = list()
        for filme in data:
            filmes.append({
                    "título": filme.titulo, 
                    "gênero": filme.genero, 
                    "ano": filme.ano
            })

        return make_response(
            jsonify(
                mensagem="Lista de filmes", 
                filmes=filmes
            )
        )

    def create_filme(self, request):
        filme = request.json
        self.filme_repository.insert(
            filme['titulo'], 
            filme['genero'], 
            filme['ano']
        )

        return make_response(
            jsonify(
                mensagem='Novo filme adicionado com sucesso!',
                filme=filme
            )
        )
