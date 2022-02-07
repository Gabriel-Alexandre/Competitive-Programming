def StringChallenge(sen):
  EXPT = '!@#?$%&*()_;.,:'
  aux = ''
  words = []

  for c, v in enumerate(sen):
    if v == ' ':
      words.append(aux)
      aux = ''
      continue
    if v in EXPT:
      continue
    aux += v

  words.append(aux)

  max_tam = 0
  word = ''
  for v in (words):
    if len(v) > max_tam:
      max_tam = len(v)
      word = v

  return word


# keep this function call here
print(StringChallenge("fun&!! time"))
