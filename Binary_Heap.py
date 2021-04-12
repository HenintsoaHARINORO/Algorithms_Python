class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percolateUp(self, i):  # i:index of items in a tree
        while i // 2 > 0:  # stops when it reaches the root element
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]  # swap
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2  # i percolates to a new level of the tree

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percolateUp(self.currentSize)

    def percolateDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
