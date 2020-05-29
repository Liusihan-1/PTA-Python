x = int(input())
q = []
for y in range(x):
    n = int(input())
    a = []
    count = 0
    for i in range(n):
        s = input()
        a.append([int(n) for n in s.split()])
    for j in range(n):
        for k in range(n):
            if j > k:
                if a[j][k] == 0:
                    count += 1
    if count == n * (n - 1) / 2:
        q.append(1)
    else:
        q.append(0)
for z in range(x):
    if q[z] == 1:
        print("YES")
    else:
        print("NO")

