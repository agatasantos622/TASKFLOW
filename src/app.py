from flask import Flask, render_template 

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/nova-tarefa")
def nova_tarefa():
    return render_template("nova_tarefa.html")

@app.route("/tarefas")
def tarefas():

    tarefas = [
        {
            "titulo": "Estudar Flask",
            "descricao": "Criar primeira aplicação.",
            "status": "Em andamento"
        },
        {
            "titulo": "Atualizar LinkedIn",
            "descricao": "Adicionar o projeto TaskFlow.",
            "status": "Concluída"
        },
        {
            "titulo": "Estudar SQL",
            "descricao": "Revisar comandos SELECT.",
            "status": "Pendente"
        }
    ]

    return render_template(
        "tarefas.html",
        tarefas=tarefas
    )

if __name__ == "__main__":
    app.run(debug=True)