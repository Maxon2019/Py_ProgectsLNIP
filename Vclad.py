s = int(input('Enter sum: ''\n'))
m = int (input('Enter months: ''\n'))
gain = int(input('Enter a monthly gain:''\n'))
per = int(input('Enter an interest rate:''\n'))

def bank(s , m , gain , per):
    res = int(s * (1 + per/12/100)**m + gain*m*(1 + per/12/100)**m)
    
    return res


res = bank(s , m, gain , per)
print(res)
