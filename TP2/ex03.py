# esse aqui percorre todos os elementos da lista e usa 2 loops, o número de comparções que são feitas é maior
def num_duplicado(lista):
    duplicados = {}
    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                if lista[i] not in duplicados:
                    duplicados[lista[i]] = 2
                else:
                    duplicados[lista[i]] += 1

    return duplicados


# essa função é mais eficiente:
def num_duplicado2(lista):
    vistos = set()
    duplicados = {}

    for num in lista:
        if num in vistos:
            if num in duplicados:
                duplicados[num] += 1
            else:
                duplicados[num] = 2
        else:
            vistos.add(num)

    return duplicados


lista_teste = [22,3,5,4,1,22,5,9,8]

print("Número : qtd de repetições:", num_duplicado(lista_teste))

print("Número : qtd de repetições:", num_duplicado2(lista_teste))
