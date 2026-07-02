from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/nova-tarefa", methods=["GET", "POST"])
def nova_tarefa():

    if request.method == "POST":

        tarefa = {
            "titulo": request.form["titulo"],
            "descricao": request.form["descricao"],
            "status": request.form["status"]
        }

        tarefas.append(tarefa)

        return redirect(url_for("listar_tarefas"))

    return render_template("nova_tarefa.html")

@app.route("/excluir/<int:id>")
def excluir_tarefa(id):

    tarefas.pop(id)

    return redirect(url_for("listar_tarefas"))

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_tarefa(id):

    if request.method == "POST":

            tarefas[id]["titulo"] = request.form["titulo"]
            tarefas[id]["descricao"] = request.form["descricao"]
            tarefas[id]["status"] = request.form["status"]

            return redirect(url_for("listar_tarefas"))

    tarefa = tarefas[id]

    return render_template(
        "editar_tarefa.html",
        tarefa=tarefa
    )

@app.route("/tarefas")
def listar_tarefas():

    return render_template(
        "tarefas.html",
        tarefas=tarefas
    )

if __name__ == "__main__":
    app.run(debug=True)