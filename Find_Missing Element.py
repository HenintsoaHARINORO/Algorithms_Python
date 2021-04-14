import collections


def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    print(arr1[-1])  # the last element of the first array


# zip([1,2,3],[4,5,6])
# [(1,4),(2,5),(3,6)] list of tuples
# num1 first number of the first array
# num2 first number of the second array
def finder2(arr1, arr2):
    d = collections.defaultdict(int)  # key is in the dictionary,default dictionary
    for num in arr2: # how many times an element shows up
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
           print(num)
        else:
            d[num] -= 1
def finder3(arr1,arr2):
    result=0

    #Perform an XOR between the numbers in the arrays
    for num in arr1+arr2: #concatenate the arrays
        result^=num
    print(result)

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [3, 7, 2, 1, 4, 6]
    finder3(arr1, arr2)
