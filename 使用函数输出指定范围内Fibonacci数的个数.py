def fib(n):
    if(n==0)or(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
def PrintFN(m,n):
    a=[]
    for i in range(25):
        if m<=fib(i)<=n:
            a.append(fib(i))
    return a

