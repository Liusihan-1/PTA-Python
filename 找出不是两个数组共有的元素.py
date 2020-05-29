c=[]
k = 0
flag = 1
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = a[0]
n = b[0]
a = a[1:]
b = b[1:]
for i in range(0, m):
    for j in range(0,n):
        if (int(a[i]) == int(b[j])):
            flag=0
            break
    if (flag==1):
        c.append(a[i])
        k=k+1
    flag=1
for i in range(0,n):
    for j in range(0,m):
        if (int(b[i]) == int(a[j])):
            flag=0
            break
    if (flag==1):
        c.append(b[i])
        k=k+1
    flag=1
res = list(set(c))
res.sort(key = c.index)
print(res[0],end="")
for i in range(1,len(res)):
    print(' {:d}'.format(res[i]),end="")
