def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]  # elements that are less or equal than the pivot
        print(less)
        greater = [i for i in arr[1:] if i > pivot]  # elements that are greater than the pivot
        print(greater)
        return quickSort(less) + [pivot] + quickSort(greater)


if __name__ == '__main__':
    print(quickSort([2, 5, 8, 3, -3]))
