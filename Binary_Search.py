def binary_search_Index(list, item):
    firstIndex = 0
    lastIndex = len(list) - 1
    while firstIndex <= lastIndex:
        middle = (firstIndex + lastIndex) // 2
        guess = list[middle]
        if guess == item:
            return middle
        if guess > item:
            lastIndex = middle - 1  # go back to while loop
        else:
            firstIndex = middle + 1
    return None


if __name__ == '__main__':
    list = [1, 3, 5, 7, 9, 12, 34]
    print(binary_search_Index(list, 3))
