num = int(input())
cnt = 0 
M = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'] 
quan = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
for i in range(num):
    flag = 1 
    jy = input() 
    pd = jy[-1] 
    sum = 0 
    for i in range(17):
        if '0' <= jy[i] <= '9':
            sum = sum + int(jy[i]) * quan[i]
        else:
            flag = 0
    if flag == 1:
        x = sum % 11
        if M[x] != pd:
            flag = 0
    if flag == 0:
        print(jy)
    else:
        cnt = cnt + 1
if cnt == num:
    print("All passed")
