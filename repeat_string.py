# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e

def repeat_str(repeat, string):
    res = '';
    for i in range (repeat):
        res = res + string
    return res

print(repeat_str(6, 'win'))
