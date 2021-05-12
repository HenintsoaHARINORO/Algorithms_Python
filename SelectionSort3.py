def selectionSort(array):
    for fillslots in range(len(array) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslots + 1):
            if array[location] > array[positionOfMax]:
                positionOfMax = location
        temp = array[fillslots]
        array[fillslots] = array[positionOfMax]
        array[positionOfMax] = temp


