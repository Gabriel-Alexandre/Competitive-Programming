def solution(inputArray):
    total = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            aux = (inputArray[i - 1] - inputArray[i]) + 1
            inputArray[i] += aux
            total += aux
    return total


print(solution([1, 1, 1]))
print(solution([-1000, 0, -2, 0]))
