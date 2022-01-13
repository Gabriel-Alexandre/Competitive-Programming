def isCrescent(sequence):
    for c, v in enumerate(sequence):
        if c == 0:
            continue
        if not v > sequence[c - 1]:
            return False
    return True

# [10, 1,2,3,4,5]
# [1, 3, 2, 1]
# [1, 3, 2, 4]
# [1, 2, 3, 4, 3, 6]
# [3, 5, 67, 98, 3]

def solution(sequence):
    if isCrescent(sequence):
        return True
    else:
        for c, v in enumerate(sequence):
            if c == 0:
                continue
            if v > sequence[c - 1]:
                continue
            else:
                copy = sequence[::]
                copy.pop(c)
                sequence.pop(c-1)
                if isCrescent(sequence) or isCrescent(copy):
                    return True
                else:
                    return False


print(solution([3, 5, 67, 98, 3]))
