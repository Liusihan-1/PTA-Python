def CountDigit(num, dig):
    cnt=0
    if(num<0):
        t=-num
    else:
        t=num
    while(t>0):
        i=t%10
        if(i==dig):
            cnt=cnt+1
        t=t//10
    return cnt
