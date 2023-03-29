def high_and_low(numbers):
    strs = numbers.split(" ")
    nums = list(map(lambda x: int(x), strs))
    max_number = max(nums)
    min_number = min(nums)
    return str(max_number) + ' ' + str(min_number)
