def soma(vetor, tamanho):
    if tamanho == 0:
        return 0
    return vetor[tamanho - 1] + soma(vetor, tamanho - 1)

vetor = [5,4,12,3,2,12]

tamanho = len(vetor)
resultado = soma(vetor, tamanho)

print(resultado)
