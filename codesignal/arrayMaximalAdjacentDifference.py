def solution(inputArray):
    maior = inputArray[1] - inputArray[0]
    for c in range(1, len(inputArray)):
        if abs(inputArray[c] - inputArray[c - 1]) > maior:
            maior = abs(inputArray[c] - inputArray[c-1])
        else:
            ...

    return maior


print(solution([2, 4, 1, 0]))
