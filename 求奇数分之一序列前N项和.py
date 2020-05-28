N=int(input())
t=1
a=1
sum=0
for i in range(1,N+1):
    sum=sum+t
    a=a+2
    t=1/a
print("sum = {:.6f}".format(sum))
