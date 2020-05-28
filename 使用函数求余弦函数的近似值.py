import math
 
 
def funcos(eps, x):
    s = 0
    i = 0
    while True:
        temp = ((-1) ** (i / 2)) * (x ** i) / math.factorial(i)
        if abs(temp) >= eps:
            s += temp
        elif abs(temp) < eps:
            break
        i += 2
    return s
