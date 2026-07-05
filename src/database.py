import sqlite3

NOME_BANCO = "taskflow.db"

def criar_banco():

    conexao = sqlite3.connect(NOME_BANCO)

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            titulo TEXT NOT NULL,

            descricao TEXT NOT NULL,

            status TEXT NOT NULL

        )
    """)

    conexao.commit()

    conexao.close()

def adicionar_tarefa(titulo, descricao, status):

    conexao = sqlite3.connect(NOME_BANCO)

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO tarefas (titulo, descricao, status)
        VALUES (?, ?, ?)
        """,
        (titulo, descricao, status)
    )

    conexao.commit()

    conexao.close()

def listar_tarefas():

    conexao = sqlite3.connect(NOME_BANCO)

    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()

    conexao.close()

    return tarefas

def excluir_tarefa(id):

    conexao = sqlite3.connect(NOME_BANCO)

    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )

    conexao.commit()

    conexao.close()

def editar_tarefa(id, titulo, descricao, status):

    conexao = sqlite3.connect(NOME_BANCO)

    cursor = conexao.cursor()

    cursor.execute(
        """
        UPDATE tarefas
        SET titulo = ?, descricao = ?, status = ?
        WHERE id = ?
        """,
        (titulo, descricao, status, id)
    )

    conexao.commit()

    conexao.close()

def concluir_tarefa(id):

    conexao = sqlite3.connect(NOME_BANCO)

    cursor = conexao.cursor()

    cursor.execute(
        """
        UPDATE tarefas
        SET status = ?
        WHERE id = ?
        """,
        ("concluida", id)
    )

    conexao.commit()

    conexao.close()
    
def buscar_tarefa(id):

    conexao = sqlite3.connect(NOME_BANCO)

    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (id,)
    )

    tarefa = cursor.fetchone()

    conexao.close()

    return tarefa

