from flask import Flask, make_response, jsonify, request
from controllers.filmes_controller import FilmeController

# ------------------------- Controladores -------------------------
filme_controller = FilmeController()

# ----------------------------- Flask -----------------------------
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

# ------------------- Rotas e métodos da API -------------------
# FILMES [GET - TITLE]
@app.route('/cinema/filmes/<titulo>')
def get_filme_by_title(titulo):
    return filme_controller.get_filme_by_title(titulo)

# FILMES [GET - LIST]
@app.route("/cinema/filmes", methods=["GET"])
def get_all_filmes():
    return filme_controller.get_all_filmes()

# FILMES [POST]
@app.route("/cinema/filmes", methods=["POST"])
def create_filme():
    return filme_controller.create_filme(request)

# ----------------------------- Executa o Flask -----------------------------
app.run()
