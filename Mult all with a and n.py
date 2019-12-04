a = float(input('Print "a": '))
n = int(input('Print"n": '))
if a > n:
    print('Print a < n')
    a = float(input('Print "a": '))
    n = int(input('Print"n": '))

def mult(a, n):
    mult_all = 1
    a1 = a
    while a1 < (a + n - 1):
        mult_all *= a1
        a1 += 1
    return mult_all
print(mult(a, n))
