import math

a,b,c=map(float,input().split())

A=a*math.pow(1+c,b)-a

print("interest=%.2f" % A)
