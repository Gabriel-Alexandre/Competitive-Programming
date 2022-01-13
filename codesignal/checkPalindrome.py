def solution(inputString):
    if inputString == inputString[::-1]:
        return True
    return False


print(solution('ana'))
