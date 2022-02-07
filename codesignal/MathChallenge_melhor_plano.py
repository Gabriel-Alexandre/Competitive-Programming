def MathChallenge(num):

  fib = [0, 1]
  for c, v in enumerate(range(num)):
    if fib[-1] > num:
      break
    if c > 1:
      n = fib[c - 1] + fib[c - 2]
      fib.append(n)
    else:
      continue
  if num in fib:
    return True
  else:
    return False


# keep this function call here
print(MathChallenge(34))

