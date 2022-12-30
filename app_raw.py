from flask import Flask, make_response, jsonify, request
from controllers.filmes_controller import FilmeController

# ------------------------- Controladores -------------------------
filme_controller = FilmeController()

# ----------------------------- Flask -----------------------------
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

# ------------------- Rotas e métodos da API -------------------
# FILMES [POST]
@app.route("/cinema/filmes", methods=["POST"])
def create_filme():
    return filme_controller.create_filme(request)

# FILMES [PUT]
@app.route("/cinema/filmes", methods=["PUT"])
def update_filme():
    return filme_controller.update_filme(request)

# FILMES [GET - LIST]
@app.route("/cinema/filmes", methods=["GET"])
def get_all_filmes():
    return filme_controller.get_all_filmes()

# FILMES [GET - TITLE]
@app.route('/cinema/filmes/<titulo>', methods=["GET"])
def get_filme_by_title(titulo):
    return filme_controller.get_filme_by_title(titulo)

# FILMES [DELETE]
@app.route('/cinema/filmes/<titulo>', methods=["DELETE"])
def delete_filme(titulo):
    return filme_controller.delete_filme(titulo)

# ----------------------------- Executa o Flask -----------------------------
app.run()
