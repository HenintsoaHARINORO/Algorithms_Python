def minimumSwaps(arr):
    swap=0
    for i in range (len(arr)):
        if(arr[i]!=(i+1)):
            t=i
            while(arr[t]!=(i+1)):
                t+=1
            temp=arr[t]
            arr[t]=arr[i]
            arr[i]=temp
            swap+=1
    return swap


def minimumSwaps(arr):
    swaps = 0

    getIndex = dict(zip(arr, range(1, len(arr) + 1)))
    for i in range(1, len(arr) + 1):
        # swap only if value is not equal to index
        if getIndex[i] != i:
            getIndex[arr[i - 1]] = getIndex[i]
            arr[getIndex[i] - 1] = arr[i - 1]
            swaps += 1
    return swaps