import random

def quickselect(arr, k):
    pivo = random.choice(arr)
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]

    if k <= len(menores):
        return quickselect(menores, k)
    elif k <= len(menores) + len(iguais):
        return pivo
    else:
        return quickselect(maiores, k - len(menores) - len(iguais))

arr = [7, 2, 1, 5, 4]
k = 3
print(f"O {k}º menor elemento é: {quickselect(arr, k)}")


# o quick select é bom porque ele tem como foco encontrar k-ésimo ( posição de um elemento em uma sequência ordenada) menor elemento, sem precisar ordenar tudo.
# a busca linear percorre elemento a elemento, isso faz com que o desempenho dela não seja tão bom com listas grandes em comparação com o quick select