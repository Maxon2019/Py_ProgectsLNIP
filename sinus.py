import math
num = int(input('Введите в градусах: '))


def sinus(num):
    y = 0.1
    sum_all = 0
    pi = 3.14
    if num <=0:
        print('Error')
    else:
        num = (num*pi) / 180

    while y < num:
        z = math.sin(y)
        y = y + 0.1
        sum_all = z + sum_all

    return sum_all
    
print(sinus(num))
