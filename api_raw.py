from flask import Flask, make_response, jsonify, request
from python_sql_alchemy.repository.filmes_repository import FilmeRepository
from python_sql_alchemy.repository.atores_repository import AtoresRepository

# ------------------------- Repositórios -------------------------
filme_repository = FilmeRepository()
atores_repository = AtoresRepository()

# ----------------------------- Flask -----------------------------
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

# ------------------- Rotas e métodos da API -------------------
# ------------------------ FILMES [GET] ------------------------
@app.route("/cinema/filmes", methods=["GET"])
def get_all_filmes():
    data = filme_repository.select_all()
    print(data)
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

# ------------------------ FILMES [POST] ------------------------
@app.route("/cinema/filmes", methods=["POST"])
def create_filme():
    filme = request.json
    filme_repository.insert(filme['titulo'], filme['genero'], filme['ano'])
    return make_response(
        jsonify(
            mensagem='Novo filme adicionado com sucesso!',
            filme=filme
        )
    )

# ----------------------------- Executa o Flask -----------------------------
app.run()
