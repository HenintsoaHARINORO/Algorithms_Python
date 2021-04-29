# return the Fibonacci values at the nth position
def fib_rec(nth):
    if nth == 0 or nth == 1:
        return nth
    else:
        return fib_rec(nth - 1) + fib_rec(nth - 2)


print(fib_rec(4))
