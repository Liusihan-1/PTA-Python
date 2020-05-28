def fib(n):
    x,y=0,1
    while(n):
        x,y,n=y,x+y,n-1
    return x
n=int(input())
sum = 0
for i in range(1,n+1):
    a = fib(i+2) / fib(i+1)
    sum = sum + a
print('{:.2f}'.format(sum))
