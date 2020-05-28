s = input()
s=s.replace('#','')
t=""
for n in s:
    if(n.islower()):
        t=t+n.upper()
    elif(n.isupper()):
        t=t+n.lower()
    else:
        t=t+n
print(t)
