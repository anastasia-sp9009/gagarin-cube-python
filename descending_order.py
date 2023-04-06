def descending_order(num):
    digitsStr = str(num)
    digits =  list(digitsStr)
    digits.reverse()
    reversedNum = "".join(digits)
    return int(reversedNum)
