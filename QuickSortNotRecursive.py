def quick_sort(array):
    quick_sort_help(array,0,len(array)-1)
def quick_sort_help(array,first,last):
    if first < last:
        splitpoint = partition(array,first,last)
        quick_sort_help(array,first,splitpoint - 1)
        quick_sort_help(array,splitpoint + 1,last)
def partition(array,,first,last):

