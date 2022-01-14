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


solution('foo(bar(baz))blim')
