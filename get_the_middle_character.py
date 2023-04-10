# https://www.codewars.com/kata/56747fd5cb988479af000028
import math
def get_middle(s):
    chars = list(s)
    count = len(chars)
    if count % 2:
        midIndex = math.floor(count / 2)
        return s[midIndex]
    if count % 2 == 0:
        midIndex = int(count / 2) - 1
        return s[midIndex] + s[midIndex + 1]

print(get_middle("sos"))
print(get_middle("best"))