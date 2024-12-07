def contar_repeticoes(string, caractere):
    if not string:
        return 0
    return (1 if string[0] == caractere else 0) + contar_repeticoes(string[1:], caractere)

resultado = contar_repeticoes("banana", "a")
print(f"{resultado} repetições ")
