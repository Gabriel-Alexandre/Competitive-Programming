def solution(picture):
    for c, l in enumerate(picture):
        picture[c] = '*' + l + '*'
    size_coluna = len(picture[0])
    picture.insert(0, ('*' * size_coluna))
    picture.append(('*' * size_coluna))
    return picture


solution(["abc", "ded"])
