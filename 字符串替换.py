a = input()
b = []
for n in a :
   if"A" <= n <= "Z" :
      b.append(chr(155-ord(n)))
   else:
      b.append(n)
print("".join(b))
