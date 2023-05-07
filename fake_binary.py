#https://www.codewars.com/kata/57eae65a4321032ce000002d
def fake_bin(x):
    list_x = list(x)
    s = []
    for i in x:
        if int(i) >= 5:
            s.append('1')
        else:
            s.append('0')
    return ''.join(s)

