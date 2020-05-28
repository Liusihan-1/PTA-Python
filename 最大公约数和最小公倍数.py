def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)
n , m = input().split()
n = int(n)
m = int(m)
print('{:d} {:d}'.format(gcd(n,m),n*m//gcd(n,m)))
