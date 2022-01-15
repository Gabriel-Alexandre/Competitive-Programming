def solution(a, b):
    if a == b:
        return True
    new_a = []
    new_b = []

    for i in range(0, len(a)):
        if a[i] != b[i]:
            new_a.append(a[i])
            new_b.append(b[i])
    new_b = new_b[::-1]

    if len(new_a) == 2 and new_a == new_b:
        return True
    return False


# print(solution([1, 2, 3], [1, 2, 3]))
print(solution([1, 2, 3], [2, 1, 3]))
print(solution([4, 6, 3], [3, 4, 6]))
print(solution([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]))
