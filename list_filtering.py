# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def filter_list(l):
    nums = list(filter(lambda x: isinstance(x, int), l))
    # nums = list(filter(lambda x: type(x) == int, l))
    return nums

print(filter_list([3, 'a', 5, 7, [], 'Hello world', 90]))