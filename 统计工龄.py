n=int(input())
lst = list(map(int,input().split()))
d = {}
for x in range(0,n):
    if not lst[x] in d:
        d[lst[x]] = 1
    else:
        d[lst[x]] = d[lst[x]] + 1
for k in sorted(d.keys()):
    print(k,end=':')
    print(d[k])
