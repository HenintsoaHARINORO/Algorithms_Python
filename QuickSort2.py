def quick_sort(array):
    quick_sort_help(array, 0, len(array) - 1)


def quick_sort_help(array, first, last):
    if first < last:
        splitpoint = partition(array, first, last)
        quick_sort_help(array, first, splitpoint - 1)
        quick_sort_help(array, splitpoint + 1, last)


def partition(array, first, last):
    pivot = array[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <=rightmark and array[leftmark] <=pivot:
            leftmark +=1
        while array[rightmark] >= pivot and rightmark >=leftmark:
            rightmark -=1

        if rightmark < leftmark:
            done = True
        else:
            temp =array[leftmark]
            array[leftmark] = array[rightmark]
            array[rightmark] = temp

    temp = array[first]
    array[first] =array[rightmark]
    array[rightmark] = temp
    return  rightmark

array = [1,-7,25,15,0]
quick_sort(array)
print(array)