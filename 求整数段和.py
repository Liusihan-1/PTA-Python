a, b = map(int, input().split())
sum = 0
i = 0
while a <= b:
    print('{:5}'.format(a), end='')
    i += 1
    if i % 5 == 0 or a == b:
        print()
    sum += a
    a += 1
print("Sum =", sum)
