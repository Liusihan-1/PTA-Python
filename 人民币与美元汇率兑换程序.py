try:
    money=input()
    if money [0] in ['￥']:
        M = eval(money.strip('￥')) / 7
        print('${:.2f}'.format(M))
    elif money[0] in ['$']:
        M= eval(money.strip('$'))*7
        print('￥{:.2f}'.format(M))
    else:
        print('输入格式错误')
except NameError:
    print('输入格式错误')
