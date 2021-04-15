def binary_search_Index(list, item):
    firstIndex = 0
    lastIndex = len(list) - 1
    while firstIndex <= lastIndex:
        lastElement = firstIndex + lastIndex
        guess = list[lastElement]
        if guess == item:
            return lastElement
        if guess > item:
            lastIndex = lastElement - 1 # go back to while loop
        else:
            firstIndex = lastElement + 1
    return None


if __name__ == '__main__':
    list = [1, 3, 5, 7, 9]
    print(binary_search_Index(list, 3))
