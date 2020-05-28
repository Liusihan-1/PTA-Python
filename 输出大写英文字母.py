a=list(input())
b=[]
for n in a:
    if n.isupper() and n not in b:
        b.append(n)
if len(b)>0:
    print(''.join(b))
else:
    print('Not Found')
