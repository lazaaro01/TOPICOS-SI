from collections import deque

class Tarefa:
    def __init__(self, titulo, prioridade):
        self.titulo = titulo
        self.prioridade = prioridade

    def __repr__(self):
        return f"Tarefa('{self.titulo}', prioridade={self.prioridade})"


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.historico = []
        self.fila_pendentes = deque()

    def adicionar_tarefa(self, titulo, prioridade):
        tarefa = Tarefa(titulo, prioridade)
        self.tarefas.append(tarefa)
        self.fila_pendentes.append(tarefa)
        print(f"Tarefa adicionada: {tarefa}")

    def remover_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                self.tarefas.remove(tarefa)
                self.historico.append(tarefa)

                if tarefa in self.fila_pendentes:
                    self.fila_pendentes.remove(tarefa)

                print(f"Tarefa removida: {tarefa}")
                return
        raise ValueError("Tarefa não encontrada.")

    def desfazer_ultima_remocao(self):
        if not self.historico:
            print("Nada para desfazer.")
            return

        tarefa_restaurada = self.historico.pop()
        self.tarefas.append(tarefa_restaurada)
        self.fila_pendentes.appendleft(tarefa_restaurada)

        print(f"Tarefa restaurada: {tarefa_restaurada}")

    def processar_tarefa(self):
        """Remove e processa a próxima tarefa da FILA FIFO."""
        if not self.fila_pendentes:
            print("Nenhuma tarefa pendente na fila.")
            return

        tarefa = self.fila_pendentes.popleft()
        print(f"Processando tarefa: {tarefa}")

    def mostrar_fila(self):
        """Exibe a fila de tarefas pendentes na ordem FIFO."""
        if not self.fila_pendentes:
            print("Fila vazia.")
            return

        print("Fila de pendências:")
        for t in self.fila_pendentes:
            print(f"- {t.titulo} (Prioridade {t.prioridade})")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        print("Todas as tarefas:")
        for t in self.tarefas:
            print(f"- {t.titulo} (Prioridade {t.prioridade})")
