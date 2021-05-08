def seq_search(array, element):
    position = 0
    found = False
    while position < len(array) and not found:
        if array[position] == element:
            found = True
        else:
            position += 1
    return found


def ordered_seq_search(array, element):
    position = 0
    found = False
    stopped = False

    while position < len(array) and not found and not stopped:
        if array[position] == element:
            found = True
        else:
            if array[position] > element:
                stopped = True
            else:
                position += 1
    return found


array = [1, 2, 3, 4, 5, 0, 9]
array2 = [0, 4, 7, 8, 12, 56, 67]
print(seq_search(array, 0))
print(ordered_seq_search(array2, 20))
