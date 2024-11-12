from typing import List

def inverter_fila(fila: List[str]) -> List[str]:
    fila.reverse()
    return fila

fila = ["Alice", "Gabriel", "Henrique", "Aline"]

novaFila = inverter_fila(fila)
print(novaFila)
