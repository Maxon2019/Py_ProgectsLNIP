plus = list(input('Print nums in plus: '))
minus = list(input('Print nums in minus: '))

def minus_plus(plus,minus):
    k = 0
    m=0
    for i in minus:
        i = int(i)
        k+=i
    for h in plus:
        h = int(h)
        m+=h
    return m - k
        



print(minus_plus(plus, minus))
        
        
