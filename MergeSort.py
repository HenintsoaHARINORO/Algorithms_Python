def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):  # check the middle
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):  # the lefthalf
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):  # the right half
            array[k] = righthalf[j]
            j += 1
            k += 1


array = [11, 2, 5, 4, 7, 6, 8, 1, 23]
merge_sort(array)
print(array)
