def isNumber(character):
  symbolList = ["+", "-", "*", "/"]
  for curSymbol in symbolList:
    if character is curSymbol:
      return False
  # Not a symbol - must be number!
  return True


def simpleTokenizer(string):
  tokenList = []
  multiNumber = False
  for symbol in string:
    # check if we found a number
    if isNumber(symbol):
      if not multiNumber:
        multiNumber = symbol
      else:
        multiNumber = multiNumber + symbol
    else:
      #found a something not a number - end current number if started
      if multiNumber:
        tokenList.append(multiNumber)
        multiNumber = False  # restart number
      # Append the found symbol
      tokenList.append(symbol)

  # End the last number
  if multiNumber:
    tokenList.append(multiNumber)

  return tokenList


print(simpleTokenizer("10+20+30*400/1000"))
