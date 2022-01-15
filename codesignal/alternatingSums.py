def solution(a):
    return [sum(a[::2]), sum(a[1::2])]


print(solution([50, 60, 60, 45, 70]))
