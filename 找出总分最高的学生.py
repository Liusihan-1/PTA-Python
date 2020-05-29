students = []
max=0
maxname=""
maxid=""
sum=0
n = int(input())
for i in range(0,n):
    t = list(map(str, input().split()))
    stuInfo = {}
    stuInfo['name'] = t[0]
    stuInfo['id'] = t[1]
    stuInfo['score1'] = int(t[2])
    stuInfo['score2'] = int(t[3])
    stuInfo['score3'] = int(t[4])
    stuInfo['sum'] = int(t[2])+int(t[3])+int(t[4])
    students.append(stuInfo)
for temp in students:
    sum=int(temp['sum'])
    if sum>max:
        max=int(temp['sum'])
        maxname=temp['name']
        maxid=temp['id']
print('{:s} {:s} {:d}'.format(maxid,maxname,max))
