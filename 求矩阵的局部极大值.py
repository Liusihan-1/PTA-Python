n, m= input().split();
n, m = int(n), int(m)
a = [];sum = 0;count=0;r=0
for i in range(n):
    s = input()
    a.append([int(n) for n in s.split()])
for i in range(1,n-1):
	for j in range(1,m-1):
		if(a[i][j]>a[i-1][j] and a[i][j]>a[i][j-1] and a[i][j]>a[i+1][j] and a[i][j]>a[i][j+1]):
				r=1
				print('{:d} {:d} {:d}'.format(a[i][j],i+1,j+1))
if(r==0):
	print('None {:d} {:d}'.format(i+2,j+2))
