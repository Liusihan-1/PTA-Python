lst = list(map(int,input().split()))
max1=max2=max3=0
for i in range(0,3):
    if(max1<lst[i]):
        max1=lst[i]
print('{:4d}{:4d}{:4d}{:4d}{:4d}'.format(lst[0],lst[1],lst[2],max1,lst[0]+lst[1]+lst[2]))
for i in range(3,6):
    if(max2<lst[i]):
        max2=lst[i]
print('{:4d}{:4d}{:4d}{:4d}{:4d}'.format(lst[3],lst[4],lst[5],max2,lst[3]+lst[4]+lst[5]))
for i in range(6,9):
    if(max3<lst[i]):
        max3=lst[i]
print('{:4d}{:4d}{:4d}{:4d}{:4d}'.format(lst[6],lst[7],lst[8],max3,lst[6]+lst[7]+lst[8]))
