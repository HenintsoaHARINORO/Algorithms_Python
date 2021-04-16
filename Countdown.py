def countDown(i):
    print(i)
    if i <= 0: # base case
        return
    else:      # recursive case
        countDown(i - 1)


if __name__ == '__main__':
    print(countDown(45))
