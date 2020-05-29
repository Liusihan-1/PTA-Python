n = int(input())
a = []
count = 0
count1 = 0
for i in range(n):
    s = input()
    a.append([int(n) for n in s.split()])
for j in range(n):
    if count1 == n and count == n:
        break
    for k in range(n):
        for k1 in range(n):
            if a[j][k] >= a[j][k1]:
                count += 1
        if count == n:
            for j1 in range(n):
                if a[j][k] <= a[j1][k]:
                    count1 += 1
            if count1 == n:
                print("{} {}".format(j, k))
                break
        count1 = 0
        count = 0
if count1 != n and count != n:
    print("NONE")
