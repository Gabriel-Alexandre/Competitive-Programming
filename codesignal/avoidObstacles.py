def solution(inputArray):
    key = True
    c = 1
    while key:
        new = list(range(0, 1000, c))
        for n, v in enumerate(inputArray):
            if v in new:
                c += 1
                break
            if n == len(inputArray) - 1:
                key = False
    return c


def solution2(inputArray):
    i = 2
    while True:
        if all(x % i != 0 for x in inputArray):
            return i
        i = i+1


print(solution2([1000, 999]))
