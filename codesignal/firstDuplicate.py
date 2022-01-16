def solution(a):
    aux = set()
    for v in a:
        if v in aux:
            return v
        else:
            aux.add(v)
    return -1


print(solution([2, 1, 3, 5, 3, 2]))
