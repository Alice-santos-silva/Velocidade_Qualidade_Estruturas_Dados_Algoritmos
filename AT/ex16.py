class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, atual, valor):
        if not atual:
            return Node(valor)
        if valor < atual.valor:
            atual.esquerda = self._inserir(atual.esquerda, valor)
        else:
            atual.direita = self._inserir(atual.direita, valor)
        return atual

    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, atual, valor):
        if not atual:
            return None
        if valor < atual.valor:
            atual.esquerda = self._remover(atual.esquerda, valor)
        elif valor > atual.valor:
            atual.direita = self._remover(atual.direita, valor)
        else:
            if not atual.esquerda: return atual.direita
            if not atual.direita: return atual.esquerda
            sucessor = self._minimo(atual.direita)
            atual.valor = sucessor.valor
            atual.direita = self._remover(atual.direita, sucessor.valor)
        return atual

    def _minimo(self, atual):
        while atual.esquerda:
            atual = atual.esquerda
        return atual

    def exibir(self):
        return self._em_ordem(self.raiz, [])

    def _em_ordem(self, atual, valores):
        if atual:
            self._em_ordem(atual.esquerda, valores)
            valores.append(atual.valor)
            self._em_ordem(atual.direita, valores)
        return valores

bst = BST()
for valor in [45, 25, 65, 20, 30, 60, 70]:
    bst.inserir(valor)
print("Inicial:", bst.exibir())
bst.remover(20)
print("Após remover 20:", bst.exibir())
bst.remover(25)
print("Após remover 25:", bst.exibir())
bst.remover(45)
print("Após remover 45:", bst.exibir())
