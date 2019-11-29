if input('Enter what do you want to conv c-f or f-c:''\n') == 'f-c':
    f = float(input('Enter farengate temp:''\n'))
    def f_c(f):
        c = int(5/9*(f-32))
        return c

    c = f_c(f)
    print(c)
elif  'c-f':
    c = float(input('Enter celcius temp:''\n'))
    def c_f(c):
        f = 9/5*c+32
        return f

    f = c_f(c)
    print(f)

else:
    print('fuck of')
    
