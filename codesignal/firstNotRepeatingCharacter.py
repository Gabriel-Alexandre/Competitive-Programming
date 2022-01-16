def solution(s):
    for v in s:
        if s.index(v) == s.rindex(v):
            return v

    return '_'

print(solution("abacabad"))