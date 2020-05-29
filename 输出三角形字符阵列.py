n=int(input())
cnt=65
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print('{:c} '.format(cnt),end="")
        cnt=cnt+1
    print("")
