class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, atual, valor):
        if valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = Node(valor)
            else:
                self._inserir(atual.esquerda, valor)
        elif valor > atual.valor:
            if atual.direita is None:
                atual.direita = Node(valor)
            else:
                self._inserir(atual.direita, valor)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, atual, valor):
        if atual is None:
            return False
        if atual.valor == valor:
            return True
        elif valor < atual.valor:
            return self._buscar(atual.esquerda, valor)
        else:
            return self._buscar(atual.direita, valor)


bst = BST()

precos = [100, 50, 150, 30, 70, 130, 170]
for preco in precos:
    bst.inserir(preco)

preco_procurado = 70
if bst.buscar(preco_procurado):
    print(f"ihuuuuuuuu! O preço {preco_procurado} está disponível.")
else:
    print(f"OPS... O preço {preco_procurado} não foi encontrado :(")

