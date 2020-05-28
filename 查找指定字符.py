a=input()
b=input()
if(b.find(a)!=-1):
    b=b[::-1]
    print('index = {:d}'.format(len(b)-b.find(a)-1))
else:
    print('Not Found')
