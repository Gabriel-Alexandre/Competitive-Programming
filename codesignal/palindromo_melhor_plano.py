def StringChallenge(strParam):
  return strParam.replace(' ', '') == strParam[::-1].replace(' ', '')

# keep this function call here
print(StringChallenge("never odd or even"))
