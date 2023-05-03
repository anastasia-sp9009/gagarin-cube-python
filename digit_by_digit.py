#https://www.codewars.com/kata/546e2562b03326a88e000020
def square_digits(num):
    num_to_str = str(num)
    list_num_to_str = list(num_to_str)
    squared = map(lambda digit: str(int(digit) ** 2), list_num_to_str)
    return int(''.join(list(squared)))

print(square_digits(9119))