from typing import List

pedidosId: List[float] = []
pedidosId.append(1)
pedidosId.append(2)
pedidosId.append(3)
pedidosId.append(4)

def qtd_impares():
    quantidade_impares = 0
    for id in pedidosId:
        if id % 2 != 0:
            quantidade_impares += 1
    return quantidade_impares

print(qtd_impares())
