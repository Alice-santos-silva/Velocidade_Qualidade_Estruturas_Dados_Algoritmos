class TabelaHash:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.tabela = [[] for _ in range(capacidade)]

    def hash(self, chave):
        return hash(chave) % self.capacidade

    def inserir(self, chave):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par == chave:
                return False
        self.tabela[indice].append(chave)
        return True

    def __str__(self):
        resultado = []
        for lista in self.tabela:
            for par in lista:
                resultado.append(f"{par}")
        return "{ " + ", ".join(resultado) + " }"


def verificar_duplicatas(lista):
    tabela_hash = TabelaHash()
    for elemento in lista:
        if not tabela_hash.inserir(elemento):
            return True
    return False

lista = [1, 2, 3, 4, 5, 2]
print("poxa :( há duplicatas" if verificar_duplicatas(lista) else "ihuuu! não há duplicatas")

lista_sem_duplicatas = [1, 2, 3, 4, 5]
print("poxa :( há duplicatas" if verificar_duplicatas(lista_sem_duplicatas) else "ihuuu! não há duplicatas")
