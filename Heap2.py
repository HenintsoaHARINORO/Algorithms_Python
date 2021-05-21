class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] *Heap.HEAP_SIZE
        self.currentPosition = -1
    def insert(self,item):
        if self.isFull():
            print("Heap is full")
            return
        self.currentPosition += 1
        self.heap[self.currentPosition] = item
        self.fixUp(self.currentPosition)

    def fixUp(self,index):
        parentIndex = int((index- 1)/2)
        while parentIndex >=0 and self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] =temp
            parentIndex= int((index-1)/2)


    def isFull(self):
        if self.currentPosition == Heap.HEAP_SIZE
            return  True
        else:
            return False



