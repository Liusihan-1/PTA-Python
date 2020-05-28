s = input()
a = reversed(list(s))
if list(a) == list(s):
    print(s)
    print("Yes")
else:
    print(s)
    print("No")
