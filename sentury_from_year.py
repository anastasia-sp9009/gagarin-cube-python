def century(year):
    import math
    return math.trunc(year/100) if year%100 == 0 else math.trunc(year/100) + 1

