def bubble_sort(array):
    for n in range(len(array) - 1, 0, -1): # from len(array)- 1 to 0 in step of -1
        print('This is the n:',n)
        for k in range(n):
            print('This is the k index check',k)
            if array[k] > array[k + 1]:
                temp = array[k]
                array[k] = array[k + 1]
                array[k + 1] = temp



array = [3, 2, -1, 0]
range(len(array) - 1, 0, -1)
print(array)
bubble_sort(array)
print(array)