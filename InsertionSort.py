def insertion_sort(array):
    for i in range(1, len(array)):
        currentValue = array[i]
        position = i
        while position > 0 and array[position - 1] > currentValue:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = currentValue


if __name__ == "__main__":
    array = [3, 4, 0, -1, 2, 123]
    insertion_sort(array)
    print(array)
