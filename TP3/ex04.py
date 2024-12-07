def fibonacci(posicao):
    if posicao <= 1: # complexidade => o(1)
        return posicao
    else:
        return fibonacci(posicao - 1) + fibonacci(posicao - 2)

n = int(input("Digite uma posição numérica: "))
resposta = fibonacci(n)
print(f'Na posição {n} o valor na sequência de fibonacci é {resposta}')

#________________________________________________________________________________________

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

for i in range(10): # complexidade => O(N)
    print("O fatorial de", i, "é", fatorial(i))
