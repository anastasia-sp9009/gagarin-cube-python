#https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def number(bus_stops):
    sum = 0
    for item in bus_stops:
        sum += item[0] - item[1]
    return sum

print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))