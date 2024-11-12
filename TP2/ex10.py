from queue import Queue

filaLivros = Queue()

filaLivros.put(1)
filaLivros.put(2)
filaLivros.put(3)
filaLivros.put(4)
filaLivros.put(5)
filaLivros.put(6)
filaLivros.put(7)

def qtd_impares(filaLivros: Queue) -> int:
    quantidade_impares = 0
    while not filaLivros.empty():
        id = filaLivros.get()
        if id % 2 != 0:
            quantidade_impares += 1
    return quantidade_impares

print(qtd_impares(filaLivros))
