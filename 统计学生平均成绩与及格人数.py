cnt = 0
res = 0
num = int(input())
if(num==0):
    print('average = 0.0')
    print('count = 0')
    exit(0)
ls = input().split()
for item in range(num):
    res += int(ls[item])
    if int(ls[item]) >= 60:
        cnt += 1
print('average = {:.1f}'.format(res/num))
print('count = {:d}'.format(cnt))
