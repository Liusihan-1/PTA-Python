a = input()
b = ''.join(a)
num= 0
sum=0
for i in range(0,len(b)):
    if(b[i]=='['):
        num+=1
    elif(b[i]==']'):
        num-=1
    if b[i].isdigit() and (i!='[') and (i!=']') and b[i]!=',' and b[i+1].isdigit()==False:
        sum = sum+num
print(sum)
