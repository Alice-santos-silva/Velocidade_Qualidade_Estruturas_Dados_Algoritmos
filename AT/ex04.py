def busca_binaria(lista, isbn, contador_binario=[0]):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        contador_binario[0] += 1
        meio = (esquerda + direita) // 2

        if lista[meio] == isbn:
            return meio
        elif lista[meio] < isbn:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

def busca_linear(lista, isbn, contador_linear=[0]):
    for i in range(len(lista)):
        contador_linear[0] += 1
        if lista[i] == isbn:
            return i
    return -1

import random
random.seed(42)

lista_isbns = sorted(random.sample(range(1, 200000), 100000))

isbn_alvo = lista_isbns[random.randint(0, 99999)]

contador_binario = [0]
indice_binario = busca_binaria(lista_isbns, isbn_alvo, contador_binario)

contador_linear = [0]
indice_linear = busca_linear(lista_isbns, isbn_alvo, contador_linear)

print(f"Busca Binária => índice {indice_binario} - {contador_binario[0]} iterações.")
print(f"Busca Linear => {indice_linear} - {contador_linear[0]} iterações.")

if contador_binario[0] < contador_linear[0]:
    print("A busca binária foi mais eficiente do que a busca linear.")
elif contador_binario[0] > contador_linear[0]:
    print("A busca linear foi mais eficiente")
else:
    print("os dois tipos tiveram o mesmo nível de eficiência")