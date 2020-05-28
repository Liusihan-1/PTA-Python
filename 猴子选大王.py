N = int(input())
t = []
for k in range(1,N+1):
    t.append(k)
cnt = 1
i = 0
while True:
    if len(t)==1:
        print(t[0])
        break
    if i==len(t):
        i = 0
    if cnt==3:
        del t[i]
        cnt = 1
    else:
        cnt += 1
        i += 1
