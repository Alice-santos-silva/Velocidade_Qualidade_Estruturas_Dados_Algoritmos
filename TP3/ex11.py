def fatorial_recursivo(c, f=1):
    print(f"{c} x " if c > 1 else f"{c} = ", end="")
    if c == 1:
        return f
    return c * fatorial_recursivo(c - 1)

n = 1000
print(f"Calculando {n}! = ", end="")

try:
    resultado = fatorial_recursivo(n)
    print(resultado)
except RecursionError:
    print("StackOverflow aconteceu! O limite de recursão foi excedido.")

# um algoritimo iterativo evitaria o estouro de pilha porque ao invés de sempre criar novas chamadas da função, usaria um laço de repetição para calcular o fatorial

# seria assim:
def fatorial_iterativo(c):
    resultado = 1
    for i in range(1, c + 1):
        resultado *= i
    return resultado

n = 1000
print(f"Calculando {n}! = ", end="")
resultado = fatorial_iterativo(n)
print(resultado)
