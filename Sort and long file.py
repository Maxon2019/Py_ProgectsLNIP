
with open('Все это тбыло бы смешно.docx','r') as file:
    f = file.read()
    
d = 0
r = 0
p = f.split()
def sal(p):
    d = max(p, key = len)
    r = min(p, key = len)
    return d , r

d = sal(p)
print(d)
