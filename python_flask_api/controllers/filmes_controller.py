from flask import make_response, jsonify
from python_sql_alchemy.repository.filmes_repository import FilmeRepository


class FilmeController:
    filme_repository = FilmeRepository()

    # CREATE FILME
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

    # LIST ALL FILMES
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

    # GET FILME BY TITULO
    def get_filme_by_title(self, titulo):
        data = self.filme_repository.select_by_title(titulo)
        filme = {
            "título": data.titulo, 
            "gênero": data.genero, 
            "ano": data.ano
        }
        return make_response(
            jsonify(
                mensagem="Filme", 
                filme=filme
            )
        )

    # DELETE FILME BY TITULO
    def delete_filme(self, titulo):
        self.filme_repository.delete(titulo)
        return make_response(
            jsonify(
                mensagem='Filme removido com sucesso!'
            )
        )
