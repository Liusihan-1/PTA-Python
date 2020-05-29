lst = list(map(int,input().split()))
for i in range(0,9,3):
    print('{:4d}'.format(lst[i]),end="")
print("")
for i in range(1,9,3):
    print('{:4d}'.format(lst[i]),end="")
print("")
for i in range(2,9,3):
    print('{:4d}'.format(lst[i]),end="")
print("")
