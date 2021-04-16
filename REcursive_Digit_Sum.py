def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


if __name__ == '__main__':
    print(sum([1, 2, 3,7,8]))
