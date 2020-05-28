a = input()
b = []
for n in a :
    if n.isdigit():
        b.append(n)
print(int("".join(b)))
