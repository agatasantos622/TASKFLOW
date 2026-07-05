import os

import pytest

from src import database


@pytest.fixture
def banco_teste():

    database.NOME_BANCO = "test_taskflow.db"

    if os.path.exists(database.NOME_BANCO):
        os.remove(database.NOME_BANCO)

    database.criar_banco()

    yield

    if os.path.exists(database.NOME_BANCO):
        os.remove(database.NOME_BANCO)

def test_criar_banco(banco_teste):

    assert os.path.exists(database.NOME_BANCO)

def test_adicionar_tarefa(banco_teste):

    database.adicionar_tarefa(
        "Estudar Pytest",
        "Criar os primeiros testes do TaskFlow",
        "pendente"
    )

    tarefas = database.listar_tarefas()

    assert len(tarefas) == 1

    assert tarefas[0]["titulo"] == "Estudar Pytest"
    assert tarefas[0]["descricao"] == "Criar os primeiros testes do TaskFlow"
    assert tarefas[0]["status"] == "pendente"

def test_buscar_tarefa(banco_teste):

    database.adicionar_tarefa(
        "Aprender Flask",
        "Estudar rotas e templates",
        "pendente"
    )

    tarefa = database.buscar_tarefa(1)

    assert tarefa is not None
    assert tarefa["id"] == 1
    assert tarefa["titulo"] == "Aprender Flask"
    assert tarefa["descricao"] == "Estudar rotas e templates"
    assert tarefa["status"] == "pendente"

def test_editar_tarefa(banco_teste):

    database.adicionar_tarefa(
        "Estudar Python",
        "Aprender funções",
        "pendente"
    )

    database.editar_tarefa(
        1,
        "Estudar Python Avançado",
        "Aprender funções e módulos",
        "em_andamento"
    )

    tarefa = database.buscar_tarefa(1)

    assert tarefa["titulo"] == "Estudar Python Avançado"
    assert tarefa["descricao"] == "Aprender funções e módulos"
    assert tarefa["status"] == "em_andamento"

def test_concluir_tarefa(banco_teste):

    database.adicionar_tarefa(
        "Finalizar README",
        "Escrever documentação",
        "pendente"
    )

    database.concluir_tarefa(1)

    tarefa = database.buscar_tarefa(1)

    assert tarefa["status"] == "concluida"

def test_excluir_tarefa(banco_teste):

    database.adicionar_tarefa(
        "Excluir tarefa",
        "Teste de exclusão",
        "pendente"
    )

    database.excluir_tarefa(1)

    tarefas = database.listar_tarefas()

    assert len(tarefas) == 0

def test_listar_tarefas(banco_teste):

    database.adicionar_tarefa(
        "Primeira tarefa",
        "Descrição da primeira tarefa",
        "pendente"
    )

    database.adicionar_tarefa(
        "Segunda tarefa",
        "Descrição da segunda tarefa",
        "em_andamento"
    )

    tarefas = database.listar_tarefas()

    assert len(tarefas) == 2

    assert tarefas[0]["titulo"] == "Primeira tarefa"
    assert tarefas[1]["titulo"] == "Segunda tarefa"