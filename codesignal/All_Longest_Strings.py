def solution(inputArray):
    maxsize = len(inputArray[0])
    arraysize = []
    for v in inputArray:
        size = len(v)
        if size > maxsize:
            maxsize = size
            arraysize.clear()
            arraysize.append(v)
        elif size == maxsize:
            arraysize.append(v)

    return arraysize


print(solution(["aba", "aa", "ad", "vcd", "aba"]))
