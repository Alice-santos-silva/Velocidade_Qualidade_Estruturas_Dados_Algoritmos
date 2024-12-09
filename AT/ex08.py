def selection_sort(jogadores):
    n = len(jogadores)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if jogadores[i]['pontuacao'] < jogadores[min_index]['pontuacao']:
                min_index = i
        if min_index != j:
            jogadores[j], jogadores[min_index] = jogadores[min_index], jogadores[j]


jogadores = [
    {"nome": "Alice", "pontuacao": 32},
    {"nome": "Gabriel", "pontuacao": 56},
    {"nome": "Aline", "pontuacao": 10},
    {"nome": "Alexia", "pontuacao": 100},
]

selection_sort(jogadores)

for jogador in jogadores:
    print(f"{jogador['nome']}: {jogador['pontuacao']} pontos")


"""
    explicação:
    o código começa com o loop principal (j) pra percorrer todos os índices dos jogadores
    o loop aninhado (i) está percorrendo para encontrar a posição onde está o menor elemento
    a parte final do código troca o elemento (j) pelo elemento que tem menor pontuação 
"""