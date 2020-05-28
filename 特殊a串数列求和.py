a,b=input().split()
a,b=eval(a),eval(b)
sum=0
t=0
for i in range(1,b+1):
    t=t*10+a
    sum=sum+t
print("s = {:d}".format(sum))
