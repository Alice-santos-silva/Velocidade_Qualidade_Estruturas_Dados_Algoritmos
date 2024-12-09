class TabelaHash:
    def __init__(self, capacidade=100):
        self.capacidade = capacidade
        self.tabela = [[] for _ in range(capacidade)]

    def hash(self, chave):
        return hash(chave) % self.capacidade

    def inserir(self, nome_usuario, perfil):
        indice = self.hash(nome_usuario)
        for par in self.tabela[indice]:
            if par[0] == nome_usuario:
                par[1] = perfil
                return
        self.tabela[indice].append([nome_usuario, perfil])

    def buscar(self, nome_usuario):
        indice = self.hash(nome_usuario)
        for par in self.tabela[indice]:
            if par[0] == nome_usuario:
                return par[1]
        return None

    def __str__(self):
        resultado = []
        for bucket in self.tabela:
            for par in bucket:
                resultado.append(f"{par[0]}: {par[1]}")
        return "{ " + ", ".join(resultado) + " }"

tabela_hash = TabelaHash()

tabela_hash.inserir("arisu", {"nome": "Alice", "idade": 22, "cidade": "Cidade Maravilhosa"})
tabela_hash.inserir("garu", {"nome": "Gabriel", "idade": 23, "cidade": "Rio de Janeiro"})
tabela_hash.inserir("Narandeiru", {"nome": "Aline", "idade": 28, "cidade": "Belo Horizonte"})

print("Buscando o perfil de arisu:")
perfil = tabela_hash.buscar("arisu")
if perfil:
    print(perfil)
else:
    print("Poxaaaa , não encontramos :(")

print("\nTabela Hash:")
print(tabela_hash)
