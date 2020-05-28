s = list(map(int,input().split()))
l=[]
for i in s:
    cnt=0
    for j in s:
        if i==j:
            cnt=cnt+1
    l.append(cnt)
max=l[0]
for i in range(len(l)):
    if l[i]>=max:
        t=i
        max=l[i]
print("{} {}".format(s[t],max))
