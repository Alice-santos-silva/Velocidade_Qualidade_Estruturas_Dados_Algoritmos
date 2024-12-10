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

    def encontrar_minimo(self):
        atual = self.raiz
        while atual and atual.esquerda:
            atual = atual.esquerda
        return atual.valor if atual else None

    def encontrar_maximo(self):
        atual = self.raiz
        while atual and atual.direita:
            atual = atual.direita
        return atual.valor if atual else None


bst = BST()

notas = [85,70,95,60,75,90,100]
for nota in notas:
    bst.inserir(nota)

minimo = bst.encontrar_minimo()
maximo = bst.encontrar_maximo()

print(f"Nota mínima: {minimo}")
print(f"Nota máxima: {maximo} - ihuuu parabéns")
