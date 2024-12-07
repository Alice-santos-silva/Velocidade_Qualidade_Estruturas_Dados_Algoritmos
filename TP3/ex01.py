import os

def listar(pasta):
    itens = os.listdir(pasta)
    for item in itens: # O(N) laço de repetição
        caminho = f"{pasta}/{item}"
        if os.path.isfile(caminho):
            print(item)
        elif os.path.isdir(caminho):
            listar(caminho)

listar("Arquivos")
