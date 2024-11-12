class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome: str):
        self.fila.append(nome)

    def atender_cliente(self):
        if self.fila:
            cliente = self.fila.pop(0)
            print(f'chegou a vez de: {cliente}')

    def tamanho_fila(self):
        return len(self.fila)

fila = FilaAtendimento()
fila.adicionar_cliente("Alice")
fila.adicionar_cliente("Henrique")
fila.adicionar_cliente("Gabriel")

fila.atender_cliente()
fila.atender_cliente()

# aqui só resta uma pessoa na fila, no caso "Gabriel"
print(fila.tamanho_fila())

