def solution(a):
    copy = [x for x in a if x > 0]
    # print(copy)
    decrescent = []
    for c in range(len(copy)):
        menor = max(copy)
        decrescent.append(menor)
        copy.remove(menor)
    # print(decrescent)
    # print(a)
    result = []
    for c, v in enumerate(a):
        if v < 0:
            result.append(v)
        else:
            result.append(decrescent.pop())
    # print(result)
    return result


print(solution([-1, 150, 190, 170, -1, -1, 160, 180]))
# print(solution())