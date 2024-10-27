def bubble_sort(lista):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        for interno in range(esquerda, direita):
            if lista[interno] > lista[interno + 1]:
                lista[interno], lista[interno + 1] = lista[interno + 1], lista[interno]

        direita -= 1

        for interno in range(direita, esquerda, -1):
            if lista[interno] < lista[interno - 1]:
                lista[interno], lista[interno - 1] = lista[interno - 1], lista[interno]

        esquerda += 1

    return lista
