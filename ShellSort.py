def shellSort(array):
    sublistCount = len(array) // 2

    while sublistCount > 0:
        for start in range(sublistCount):
            gap_insertion_sort(array, start, sublistCount)

        sublistCount = sublistCount // 2


def gap_insertion_sort(array, start, gap):
    for i in range(start + gap, len(array), gap):
        print(i)
        currentValue = array[i]
        position = i

        while position >= gap and array[position - gap] > currentValue:
            array[position] = array[position - gap]
            position = position - gap
        array[position] = currentValue


array = [23, 13, 0, -5, 3]
shellSort(array)
print(array)
