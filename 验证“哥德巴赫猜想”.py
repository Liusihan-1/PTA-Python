import math
def isPrime(n):
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        return False
  return True
x=int(input())
for y in range(2,x//2+1):
    z = x - y
    if (isPrime(y) == 1 and isPrime(z) == 1):
        print('{:d} = {:d} + {:d}'.format(x, y, z))
        break
