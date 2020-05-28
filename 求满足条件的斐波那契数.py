def fib(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = int(input())
for i in range(1, 1000):
    if fib(i) > n:
        break
print(fib(i))
