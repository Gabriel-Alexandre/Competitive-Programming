def solution(a):
    new_m = []
    new_aux = []
    for c in range(len(a)):
        for v in a[::-1]:
            new_aux.append(v[c])
        new_m.append(new_aux[::])
        new_aux.clear()

    return new_m

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(solution(a))
