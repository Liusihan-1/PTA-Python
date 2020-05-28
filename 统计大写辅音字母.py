a = input()
cnt=0
for n in a :
   if n.isupper() and n!="A" and n!="E" and n!="I" and n!="O" and n!="U":
      cnt=cnt+1
print(cnt)	
