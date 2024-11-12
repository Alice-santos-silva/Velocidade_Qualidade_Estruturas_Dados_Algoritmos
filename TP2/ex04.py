from typing import List

def pilhaCrescente(notas: List[float]) -> List[float]:
    notas.sort()
    return notas

notas = [3.5, 1.2, 4.7]
resultado = pilhaCrescente(notas)
print(resultado)
