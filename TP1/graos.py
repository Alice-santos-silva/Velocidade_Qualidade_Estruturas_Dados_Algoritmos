def graos(g):
    if g <= 0:
        return "A quantidade de grãos deve ser maior que zero."

    quadrado = 1
    while 2 ** (quadrado - 1) < g:
        quadrado += 1

    if 2 ** (quadrado - 1) == g:
        return quadrado
    else:
        return "A quantidade de grãos não corresponde a um quadrado."