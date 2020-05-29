while True:
    try:
        n=input()
        ls=n.split()
        l=len(ls)
        if l!=0:
           print("{:d}".format(l))        
    except:
        break       
