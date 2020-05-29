def change(money):
    n = int(money[1:])
    if money[0] == '$':
        print("{}美元 = {:.2f}人民币".format(n,n*6.709))
    else:
        print("{}人民币 = {:.2f}美元".format(n, n / 6.709))
