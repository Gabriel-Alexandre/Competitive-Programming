def solution(inputArray):
    maior = 0
    ant = 0
    for c, v in enumerate(inputArray):
        atual = v * ant
        if atual > maior and c > 0 or c == 1:
            maior = atual
        ant = v
    return maior


print(solution([3, 6, -2, -5, 7, 3]))
