def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return 'syntax error'
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    n = factorial(-1)
    print(n)
