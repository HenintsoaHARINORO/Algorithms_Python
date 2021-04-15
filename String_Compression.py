def compress(s):
    r = " "
    l = len(s)

    # Edge cases
    if l == 0:
        return " "
    if l == 1:
        return s + "1"

    last = s[0]
    count = 1
    i = 1
    while i < l:
        if s[i] == s[i - 1]:
            count += 1
        else:
            r = r + s[i - 1] + str(count)
            count = 1
        i += 1
    r = r + s[i - 1] + str(count)
    print(r)


if __name__ == '__main__':
    compress('qsadddde')
