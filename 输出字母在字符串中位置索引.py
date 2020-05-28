s=input()
m,n=input().split()
for i in range(len(s)-1,-1,-1):
	if s[i]==m:
		print("%d %s"%(i,m))
	if s[i]==n:
		print("%d %s"%(i,n))

