def fn(m, n):
    sum=res=0
    for i in range(1, n+1):
        sum=sum+m
        m=m*10
        res=res+sum
    return res
