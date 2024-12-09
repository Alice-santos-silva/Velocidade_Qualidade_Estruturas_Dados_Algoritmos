import os

def percorrer_arquivos(pasta):
    try:
        itens = os.listdir(pasta)
        for item in itens:
            caminho_completo = os.path.join(pasta, item)
            if os.path.isfile(caminho_completo):
                print(caminho_completo)
            elif os.path.isdir(caminho_completo):
                percorrer_arquivos(caminho_completo)
    except PermissionError:
        print(f"Permissão negada: {pasta}")


caminho_inicial = "Arquivos"
percorrer_arquivos(caminho_inicial)


"""
explicação: 
A recursão permite explorar essa estrutura diretórios e subdiretórios de forma automática.
A recursão percorre cada nível da hierarquia até alcançar os arquivos. Além disso, os 'problemas' são divididos em partes menores, o que deixa o código mais simples.
"""