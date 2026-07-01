from flask import Flask, render_template 

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/nova-tarefa")
def nova_tarefa():
    return render_template("nova_tarefa.html")

if __name__ == "__main__":
    app.run(debug=True)