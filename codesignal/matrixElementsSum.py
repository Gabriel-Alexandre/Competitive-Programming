def solution(matrix):
    soma = 0
    for cm, linha in enumerate(matrix):
        for cl, valor in enumerate(linha):
            if cm == 0 and valor > 0:
                soma += valor
                continue

            key = True
            for ct, l in enumerate(matrix):
                if l[cl] == 0 and ct < cm:
                    key = False

            if valor > 0 and key:
                soma += valor

    return soma


print(solution([[1, 1, 1, 0],
                [0, 5, 0, 1],
                [2, 1, 3, 10]]))