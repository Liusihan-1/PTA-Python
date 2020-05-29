s=input()
sum=0
t=""
flag=0
s=s=s.replace(',',' ')
s=s.replace('[',' ')
s=s.replace(']',' ')
s=s.replace('(',' ')
s=s.replace(')',' ')
for i in s:
    if(i=='"'):
        flag=flag+1
    if(flag%2==0 and i!='"'):
        t=t+i
t=t.split()
for i in range(0,len(t)):
    sum=sum+int(t[i])
print(sum)
