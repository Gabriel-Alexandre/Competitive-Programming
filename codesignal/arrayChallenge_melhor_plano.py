def ArrayChallenge(strArr):
  s1 = strArr[0].split(sep=',')
  s2 = strArr[1].split(sep=',')

  aux = ''
  for v in s1:
    if v in s2:
      aux += v + ','

  if len(aux) > 0:
    return aux
  else:
    return False


# keep this function call here
print(ArrayChallenge(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))