def solution(n):
    if n == 1:
        return 1
    result = 1
    for v in range(1, n):
        result += v * 4
    return result


print(solution(2))
