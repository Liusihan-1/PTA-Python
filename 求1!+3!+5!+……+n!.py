import math
n=int(input())
s=0
for i in range(1,n+1,2):
    s=s+math.factorial(i)
print('n={:d},s={:d}'.format(n,s))
