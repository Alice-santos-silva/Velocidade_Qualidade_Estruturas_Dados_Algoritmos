from list_comprehension import list_comprehension
from cartas_baralho import insertion_sort_cartas
from greatestNumber import  greatest_number
from graos import graos
from bubblesort import bubble_sort
from bubblesort2 import bubble_sort2
from bubblesort3 import bubble_sort3

if __name__ == '__main__':
    # exercicio 1
    print(list_comprehension())

    # exercicio 2
    cartas_embaralhadas = [7, 3, 13, 2, 11, 8, 5, 9, 12, 6, 10, 4, 1]
    insertion_sort_cartas(cartas_embaralhadas)

    # exercicio 5
    ex05 = [1, 3, 8, 3, 110, 5, 20]
    print(greatest_number(ex05))

    # exercicio 6
    print(graos(16))

    # exercicio 8:
    listaBubble = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(listaBubble))

    # exercicio 9:
    listaA = [6,4,12,32]
    listaB = [78.3234,1,23,100]
    listaC = [0,10,1000,1]
    print(bubble_sort2(listaA))
    print(bubble_sort2(listaB))
    print(bubble_sort2(listaC))

    # exercicio 10:
    listaD = ['alice', 'henrique', 'silvia', 'gabriel']
    listaE = ['terra', 'fogo', 'ar', 'agua']
    print(bubble_sort3(listaD))
    print(bubble_sort3(listaE))