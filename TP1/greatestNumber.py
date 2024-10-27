def  greatest_number(array):
    frequencia = {}
    for numero in array:
        frequencia[numero] = frequencia.get(numero, 0) + 1

    numeros_unicos = [numero for numero, contagem in frequencia.items() if contagem == 1]

    if not numeros_unicos:
        return None

    return max(numeros_unicos)
