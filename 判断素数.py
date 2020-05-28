def isPrime(num):
    num=int(num)
    for i in range(2,num):
        if num%i==0 :
            return False
    if(num!=1):
        return True
n = int(input())
for i in range(1,n+1):
    t=int(input())
    if(isPrime(t)):
        print("Yes")
    else:
        print("No")

