def bonus(sales):
    if sales>100000:
        sales=sales*0.25+5000
    elif sales>50000:
        sales=sales*0.20+5000
    elif sales>20000:
        sales=sales*0.15+5000
    elif sales>10000:
        sales=sales*0.10+5000
    else:
        sales=5000
    return sales
