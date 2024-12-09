import time
def bubble_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

lista_mil = [i for i in range(1000, 0, -1)]
inicio_mil = time.time()
bubble_sort(lista_mil)
fim_mil = time.time()
print(f"Tempo para ordenar lista com 1.000 elementos: {fim_mil - inicio_mil:.4f} segundos")

lista_dez_mil = [i for i in range(10000, 0, -1)]
inicio_dez_mil = time.time()
bubble_sort(lista_dez_mil)
fim_dez_mil = time.time()
print(f"Tempo para ordenar lista com 10.000 elementos: {fim_dez_mil - inicio_dez_mil:.4f} segundos")

# o desempenho é impactado pela entrada de dados porque entradas maiores exigem maiores recursos computacionais.