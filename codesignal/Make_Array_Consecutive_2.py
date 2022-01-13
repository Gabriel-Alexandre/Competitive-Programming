def solution(statues):
    sorted(statues)
    aux = list(range(min(statues), max(statues) + 1))
    return len(aux) - len(statues)


print(solution([6, 2, 3, 8]))
