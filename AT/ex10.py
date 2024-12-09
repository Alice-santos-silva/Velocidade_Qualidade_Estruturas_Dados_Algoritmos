class Pilha:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "A pilha está vazia"

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "A pilha está vazia"

    def size(self):
        return len(self.itens)

    def display(self):
        print("Pilha:", self.itens)


class Navegador:
    def __init__(self):
        self.histórico = Pilha()
        self.avançar = Pilha()

    def visitar_pag(self, página):
        print(f"navegando até a página: {página}")
        self.histórico.push(página)
        self.avançar = Pilha()

    def voltar(self):
        if not self.histórico.is_empty():
            página_atual = self.histórico.pop()
            self.avançar.push(página_atual)
            if not self.histórico.is_empty():
                print(f"Voltando para: {self.histórico.peek()}")
            else:
                print("as paginas acabaram")
        else:
            print("histórico vazio")

    def avancar(self):
        if not self.avançar.is_empty():
            pag_atual = self.avançar.pop()
            print(f"Avançando para: {pag_atual}")
            self.histórico.push(pag_atual)
        else:
            print("Não há mais páginas para avançar.")

    def exibir_historico(self):
        print("Histórico de navegação:")
        self.histórico.display()
        print("Páginas para avançar:")
        self.avançar.display()

navegador = Navegador()

navegador.visitar_pag("Página 1")
navegador.visitar_pag("Página 2")
navegador.visitar_pag("Página 3")

navegador.voltar()
navegador.voltar()
navegador.avancar()

navegador.visitar_pag("Página 4")
navegador.voltar()

navegador.exibir_historico()

