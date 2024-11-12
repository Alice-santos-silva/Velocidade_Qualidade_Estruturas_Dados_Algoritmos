from typing import List, Any

class Tarefas:
    def __init__(self):
        self.__data: List[Any] = []

    def push(self, item: Any) -> None:
        self.__data.append(item)

    def peek(self) -> Any:
        if not self.__data:
            return None
        return self.__data[-1]

def tarefa_no_topo(pilha_de_tarefas: Tarefas) -> Any:
    pilha_de_tarefas.push('tp1')
    pilha_de_tarefas.push('tp2')
    return pilha_de_tarefas.peek()

pilha_de_tarefas = Tarefas()

print(tarefa_no_topo(pilha_de_tarefas))