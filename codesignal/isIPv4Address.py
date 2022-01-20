def solution(inputString):
    aux = inputString.split(sep='.')
    for v in aux:
        print(v)
        if v == '' or not v.isnumeric():
            return False
        if len(v) == 2:
            if v[0] == '0':
                return False
        if len(v) == 3:
            if v[0] == '0' or (v[0] == '0' and v[1] == '0'):
                return False
        if int(v) < 0 or int(v) > 255:
            return False
    if len(aux) == 4:
        return True
    else:
        return False

print(solution("64.233.161.00"))
