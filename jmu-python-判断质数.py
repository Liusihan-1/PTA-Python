def isPrime(num):
    if not num.isdigit():
        return False
    elif int(num) == 1:
        return False
    elif int(num) == 2:
        return True
    else :
        for i in range(2,int(num)):
            if int(num) % i == 0:
                return False
        return True
