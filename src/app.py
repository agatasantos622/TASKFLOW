from flask import Flask, render_template, request, redirect, url_for
from database import (
    criar_banco,
    adicionar_tarefa,
    listar_tarefas,
    excluir_tarefa,
    editar_tarefa,
    buscar_tarefa,
    concluir_tarefa
)

app = Flask(__name__)

criar_banco()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/nova-tarefa", methods=["GET", "POST"])
def nova_tarefa():

    if request.method == "POST":

        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        status = request.form["status"]

        adicionar_tarefa(
            titulo,
            descricao,
            status
        )

        return redirect(url_for("exibir_tarefas"))

    return render_template("nova_tarefa.html")

@app.route("/excluir/<int:id>")
def remover_tarefa(id):

    excluir_tarefa(id)

    return redirect(url_for("exibir_tarefas"))

@app.route("/editar/<int:id>", methods=["GET", "POST"])

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def atualizar_tarefa(id):

    if request.method == "POST":

        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        status = request.form["status"]

        editar_tarefa(
            id,
            titulo,
            descricao,
            status
        )

        return redirect(url_for("exibir_tarefas"))

    tarefa = buscar_tarefa(id)

    return render_template(
        "editar_tarefa.html",
        tarefa=tarefa
    )

@app.route("/concluir/<int:id>")
def concluir(id):

    concluir_tarefa(id)

    return redirect(url_for("exibir_tarefas"))

@app.route("/tarefas")
def exibir_tarefas():

    tarefas = listar_tarefas()

    return render_template(
        "tarefas.html",
        tarefas=tarefas
    )

if __name__ == "__main__":
    app.run(debug=True)