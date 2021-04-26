def rec_binary_search(array, ele):
    if len(array) == 0:
        return False
    else:
        mid = len(array)//2

        if array[mid] == ele:
            return True
        else:
            if ele < array[mid]:
                return rec_binary_search(array[:mid], ele)
            else:
                return rec_binary_search(array[mid+1:], ele)
if __name__=="__main__":
    array = [1,2,3,5,6]
    print(rec_binary_search(array,5))