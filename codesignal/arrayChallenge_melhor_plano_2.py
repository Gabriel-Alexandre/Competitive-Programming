def ArrayChallenge(arr):

  rept = []
  numbers = []

  for c, v in enumerate(arr):
    if v not in numbers:
      rept.append(arr.count(v))
      numbers.append(v)

  maior = 0
  number = -1
  for c, v in enumerate(rept):
    if v > maior and v > 1:
      maior = v
      number = numbers[c]

  return number

# keep this function call here
print(ArrayChallenge([3,4,1,6,10]))

