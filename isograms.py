#https://www.codewars.com/kata/54ba84be607a92aa900000f1
def is_isogram(string):
    lower_chars = list(string.lower())
    unique_chars = list(set(lower_chars))
    return len(unique_chars) == len(lower_chars)

print(is_isogram("isIsogram"))