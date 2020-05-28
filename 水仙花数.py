import math
n=int(input())
for i in range(int(math.pow(10,n-1)),int(math.pow(10,n))):
    sum=0
    j=i
    while(j>=1):
        sum=sum+math.pow(j%10,n)
        j=j//10
    if(sum==i):
        print('{:d}'.format(i))
