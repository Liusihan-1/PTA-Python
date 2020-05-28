def fib(n):
  a, b = 0, 1
  for i in range(n + 1):
    a, b = b, a + b
  return a
n=int(input())
if(n>0):
    for i in range(0,n):
        print('{:11d}'.format(fib(i)),end="")
        if((i+1)%5==0):
            print("")
else:
    print("Invalid.")
