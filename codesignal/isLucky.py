def solution(n):
    new_number = str(n)
    size = int(len(new_number) / 2)
    n1 = new_number[:size]
    n2 = new_number[size:]
    rn1 = sum([int(item) for item in n1])
    rn2 = sum([int(item) for item in n2])
    return True if rn1 == rn2 else False


print(solution(1212))
