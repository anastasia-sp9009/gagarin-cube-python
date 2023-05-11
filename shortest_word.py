#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
def find_short(s):
    split_s = s.split()
    min_item = len(split_s[0])
    for i in split_s:
        if len(i) < min_item:
            min_item = len(i)
    return min_item

print(find_short("bitcoin take over the world maybe who knows perhaps"))