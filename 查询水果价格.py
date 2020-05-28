print("[1] apple")
print("[2] pear")
print("[3] orange")
print("[4] grape")
print("[0] exit")
lst = list(map(int,input().split()))
for i in range(0,5):
    choice = int(lst[i])
    if(choice==1):
        print("price = 3.00")
    elif(choice==2):
        print("price = 2.50")
    elif (choice == 3):
        print("price = 4.10")
    elif (choice == 4):
        print("price = 10.20")
    elif(choice == 0):
        break
    else:
        print("price = 0.00")
