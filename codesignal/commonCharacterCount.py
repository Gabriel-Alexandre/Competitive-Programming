def conta_letra(palavra):
    array_s = []
    count_s = []
    for letra in palavra:
        if not letra in array_s:
            array_s.append(letra)
            count_s.append(palavra.count(letra))

    return [array_s, count_s]


def menor(n1, n2):
    if n1 > n2:
        return n2
    else:
        return n1


def solution(s1, s2):
    array_s1 = conta_letra(s1)
    array_s2 = conta_letra(s2)
    soma = 0

    print(array_s1)
    print(array_s2)

    for c, vs1 in enumerate(array_s1[0]):
        if vs1 in array_s2[0]:
            soma += menor(array_s1[1][c], array_s2[1][array_s2[0].index(vs1)])

    return soma


# Melhor Solução:

# def solution(s1, s2):
#     com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
#     return sum(com)

print(solution("aabcc", "adcaa"))