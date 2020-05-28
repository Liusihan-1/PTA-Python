a = input()
for i in list(range(1,len(a)+1)):
    print(str(a[-i:][:1]),end='')
