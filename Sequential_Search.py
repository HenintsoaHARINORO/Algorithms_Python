def seq_search(array, element):
    position = 0
    found = False
    while position < len(array) and not found:
        if array[position] == element:
            found = True
        else:
            position += 1
    return found
