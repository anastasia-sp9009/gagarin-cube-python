#https://www.codewars.com/kata/55908aad6620c066bc00002a
def xo(s):
    lower_s = s.lower()
    x_count = lower_s.count('x')
    o_count = lower_s.count('o')
    return x_count == 0 or o_count == 0 or x_count == o_count

print(xo('xxxxxoooXooo'))