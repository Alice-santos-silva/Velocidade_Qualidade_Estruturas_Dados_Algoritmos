def quicksort(lista, inicio=0, fim=None): # O(1)
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = dividir(lista, inicio, fim) # O(n)
        quicksort(lista, inicio, p - 1)
        quicksort(lista, p + 1, fim)

def dividir(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio
    for j in range(inicio, fim): # O(n)
        if lista[j] <= pivo:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

# O(n)*O(n) => complexidade => O(n^2) exercício 6

lista = [10, 7, 8, 9, 1, 5]

quicksort(lista)
print("Lista ordenada:", lista)

# o quick sort segue a ideia de dividir para conquistar. A recursão atua ordenando as sublistas (direita  e esquerda), depois as sublistas são combinadas com o pivô na posição certa.