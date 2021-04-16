def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    print(arr)
    newArr = []
    for i in range(len(arr)):
        smallest_Index = findSmallest(arr)
        newArr.append(arr.pop(smallest_Index)) # take the smallest element from the arr and append it to the new Arr
        print(arr)
    return newArr


if __name__ == '__main__':
    print(selectionSort([1, 4, -35, 0, -2]))
