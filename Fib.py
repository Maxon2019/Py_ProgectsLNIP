g = 1
n = int(input())
p = 0
i = 0


def fib(g,p,i, n):
    i += 1
    if n == i:
        return g
    else:
        k = g
        g = g+p
        p = k
        g = fib(g, p,i,n)
        return g


print(fib(g,p,i,n))
 
