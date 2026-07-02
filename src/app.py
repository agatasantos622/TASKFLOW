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

@app.route("/tarefas")
def listar_tarefas():

    return render_template(
        "tarefas.html",
        tarefas=tarefas
    )

if __name__ == "__main__":
    app.run(debug=True)