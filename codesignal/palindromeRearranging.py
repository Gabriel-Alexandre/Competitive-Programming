def solution(inputString):
    quant = []
    letra = set()
    for v in inputString:
        if v not in letra:
            quant.append(inputString.count(v))
            letra.add(v)

    c = 0
    for v in quant:
        if v % 2 == 0:
            continue
        else:
            c += 1
        if c > 1:
            return False
    return True


def solution2(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1


print(solution("aabbbc"))

