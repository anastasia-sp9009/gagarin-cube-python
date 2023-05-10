#https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    sum_num = sum(numbers)
    average = sum_num / len(numbers)
    return average
print(find_average([1,2]))