n = input()
d = 0
r = 0
p = n.split()
def sal(p):
    d = max(p, key = len)
    r = min(p, key = len)
    return d , r

d = sal(p)
print(d)

