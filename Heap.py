from heapq import heappop, heappush, heapify

heap = []
nums = [12, 3, -2, 6, 4, 8, 9]

# for num in nums:
# heappush(heap,nums)

# while heap:
#  print(heappop(heap)) # return the root node on every iteration

heapify(nums)
print(nums)
