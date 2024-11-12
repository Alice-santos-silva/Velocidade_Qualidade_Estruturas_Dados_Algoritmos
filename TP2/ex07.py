from typing import List

pedidosId: List[float] = []
pedidosId.append(1)
pedidosId.append(2)
pedidosId.append(3)
pedidosId.append(4)
pedidosId.append(5)
pedidosId.append(6)

def qtd_pares():
    quantidade_pares = 0
    for id in pedidosId:
        if id % 2 == 0:
            quantidade_pares += 1
    return  quantidade_pares

print(qtd_pares ())
