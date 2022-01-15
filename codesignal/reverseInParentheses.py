import re


def solution(inputString):
    print(inputString)
    subs = re.findall("\((.*?)\)", inputString)
    subs_inverted = [x[::-1] for x in subs]
    result = inputString
    for c, v in enumerate(subs_inverted):
        result = result.replace(subs[c], v)
    result = result.replace('(', '')
    result = result.replace(')', '')
    print(subs)
    print(subs_inverted)
    print(result)
    return result

def sub_paret(string):
    aux_parent = []
    aux_string = ''
    aux_string_base = ''
    for v in string:
        if v == '(':
            aux_parent.append(v)
            if len(aux_parent) > 1:
                aux_string += '('
            continue
        if v == ')':
            aux_parent.pop()
            if len(aux_parent) >= 1:
                aux_string += ')'
            continue
        if len(aux_parent) > 0:
            aux_string += v

    for v in aux_string:
        if v == '(':
            aux_parent.append(v)
            continue
        if v == ')':
            aux_parent.pop()
            continue
        if len(aux_parent) == 0:
            aux_string_base += v

    novo = aux_string_base
    if '(' in aux_string:
        novo += sub_paret(aux_string)
        return novo[::-1]
    else:
        return novo[::-1]


def solution2(inputString):
    print(inputString)
    print(sub_paret(inputString))

# print(sub_paret('foo(bar(baz))blim'))
solution2('foo(bar(baz))blim')
# sub_paret('foo(bar)baz')
# solution2('foo(bar(baz))blim')
