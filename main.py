from tarefas import Tarefa, GerenciadorTarefas

from collections import deque

gerenciador = GerenciadorTarefas()

gerenciador.adicionar_tarefa("Estudar Python", 1)
gerenciador.adicionar_tarefa("Treinar", 2)

print("Erro 1: Remover uma tarefa inexistente")
try:
    gerenciador.remover_tarefa("Tarefa inválida")  

except ValueError as ValorErro:
    print(f"Erro tratado: {ValorErro}")



print("Erro 2: Tentar remover tarefa passando um tipo inválido")
try:
    gerenciador.remover_tarefa(None)  
except TypeError:
    print("Erro tratado: o título da tarefa deve ser uma string.")
except Exception as Excecao:
    print(f"Outro erro tratado: {Excecao}")

gerenciador.listar_tarefas()