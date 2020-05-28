def acronym(p):
    s=""
    p=p.title()
    a=p.split()
    for i in range(0,len(a)):
        s=s+a[i][0]
    return s
