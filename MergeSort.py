def merge_sort(array):
    if len(array) > 1:
        mid = len(array) / 2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
