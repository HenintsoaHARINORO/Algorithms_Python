def Num(n):
    if n == 0:
        return 0
    else:
        print(n)
        return Num(n - 1)


if __name__ == '__main__':
    n = Num(4)
    print(n)
