N = int(input())
t = list(map(int,input().split()))
maxnum = t[0]
index = 0
for i in range(N):
    if t[i]>maxnum:
        maxnum = t[i]
        index = i
print(maxnum,index)
