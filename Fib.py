g = int(input())


def fib(g):
    if g == 0:
        return 1
    else:
        g = fib(g+1)
    return g


print(fib(g))
