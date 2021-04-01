def isArrayInSortedOrder(arr, n):
    if n == 1:
        return 1
    else:
        if arr[n - 1] < arr[n - 2]:
            return 0
        else:
            return isArrayInSortedOrder(arr, n - 1)


if __name__ == '__main__':
    arr = [1, 2, 3,0]
    n = len(arr)
    bool = isArrayInSortedOrder(arr, n)
    print(bool)
