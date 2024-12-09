class Fila:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens.pop(0)

    def peek(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens[0]

    def size(self):
        return len(self.itens)

    def display(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:", end=" ")
            for item in self.itens:
                print(item, end=" ")
            print()

class atender_chamados:
    def __init__(self):
        self.fila_chamados = Fila()

    def novo_chamado(self, chamado):
        print(f"Novo chamado recebido: {chamado}")
        self.fila_chamados.enqueue(chamado)

    def atender_chamado(self):
        if self.fila_chamados.is_empty():
            print("Nenhum chamado para atender.")
        else:
            chamado = self.fila_chamados.dequeue()
            print(f"Atendendo chamado: {chamado}")

    def exibir_chamados(self):
        print("Chamados na fila:")
        self.fila_chamados.display()


sistema = atender_chamados()

sistema.novo_chamado("alice está com problemas ")
sistema.novo_chamado("gabriel está com problemas")

sistema.exibir_chamados()

sistema.atender_chamado()
sistema.atender_chamado()

sistema.exibir_chamados()

sistema.atender_chamado()
