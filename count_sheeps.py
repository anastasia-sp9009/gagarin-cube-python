# https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(sheep):
    counter = 0
    for item in sheep:
        if item == True:
            counter += 1
    return counter
