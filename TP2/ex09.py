lista = [4, 3, 1, 2, 7, 54, 21]
# usei o bubble sort pra comparar numero a numero
for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)
