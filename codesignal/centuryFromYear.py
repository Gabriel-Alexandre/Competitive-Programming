def solution(year):
    result = ((year - 1) // 100) + 1
    if not result:
        return 1
    return result


print(solution(2001))
