#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
def accum(s):
    chars = list(s)
    parts = []
    for i in range(len(chars)):
        part = chars[i] * (i + 1)
        parts.append(part[0].upper() + part[1:].lower())
    return '-'.join(parts)

# accum("abcd") -> "A-Bb-Ccc-Dddd"
print(accum("HbideVbxncC"))