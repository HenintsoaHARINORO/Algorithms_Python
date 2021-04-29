def fib_iterative(nth):
    a = 0
    b = 1
    for i in range(nth):
        a, b = b, a + b
    return a
