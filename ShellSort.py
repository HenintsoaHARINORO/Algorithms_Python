def shellSort(array):
   sublistCount = len(array) // 2

   while sublistCount > 0:
       for start in range(sublistCount):
           gap_insertion_sort(array,start,sublistCount)

       sublistCount = sublistCount // 2
def gap_insertion_sort(array,start,gap):
