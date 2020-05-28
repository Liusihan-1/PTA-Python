a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if(a+b>c and b+c>a and a+c>b):
    print("yes")
else:
    print("no")
