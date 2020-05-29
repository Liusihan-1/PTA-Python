year=int(input())
if(year%400 == 0)or(year%100 !=0 and year%4 == 0):
    print('%d是闰年'%year)
else:
    print('%d不是闰年'%year)
