def bubble_sort2(lista):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista