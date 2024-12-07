def torre_hanoi(n, tinicial, auxiliar, tfinal):
    if n == 1:
        print(f'mover disco 1  da torre {tinicial} para a torre {tfinal}')
        return
    torre_hanoi(n-1, tinicial, tfinal,auxiliar)
    print(f'mover disco {n}  da torre {tinicial} para a torre {tfinal}')
    torre_hanoi(n - 1, auxiliar, tinicial, tfinal)

n_discos = 3
torre_hanoi(n_discos, 'A', 'B', 'C')

# o caso base de recursão na torre de hanoi  é mover uma única peça para a torre de destino final, e as demais para a torre auxiliar.
# A cada chamada de recursão, o problema vai ficando menor até atingir o caso base (inicial) em que o número de discos é igual a  1. Esse caso base é resolvido com uma operação  (mover um disco entre duas torres).