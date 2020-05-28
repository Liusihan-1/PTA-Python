e = float(input())
a = 1
i = 2
t = 2
b = 1 / t
sum = 1 + 1
e1 = 1
e2 = sum
while e2 - e1 >= e:
    e1 = e2
    a = b
    sum = sum + a
    e2 = sum
    i = i + 1
    t = t * i
    b = 1 / t
print('{:.6f}'.format(sum))
