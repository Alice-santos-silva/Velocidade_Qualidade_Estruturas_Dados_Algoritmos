def insertion_sort_cartas(cartas):
    for i in range(1, len(cartas)):
        carta_atual = cartas[i]
        j = i - 1

        while j >= 0 and cartas[j] > carta_atual:
            cartas[j + 1] = cartas[j]
            j -= 1

        cartas[j + 1] = carta_atual

    print(cartas)