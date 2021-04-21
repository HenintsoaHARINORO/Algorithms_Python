def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        remainder = num1 % num2
        return gcd(num2, remainder)


if __name__ == "__main__":
    print(gcd(1482, 819))
