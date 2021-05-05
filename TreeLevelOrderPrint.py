import collections
from collections import deque


class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


def levelOrderPrint(tree):
    if tree is None:
        return None
    queue = deque()  # why deque?because it has two ends
    queue.append(tree)
    while len(queue) != 0:
        temp = deque()
        while len(queue) != 0:
            node = queue.pop()
            print(str(node.value) + ' ')
            if node.left is not None:
                temp.append(tree.left)
            if node.right is not None:
                temp.append(tree.right)
            queue = temp


def levelOrderPrint2(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount = 1
    nextCount = 0
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        print(currentNode.value, )
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        if currentCount == 0:
            currentCount = nextCount,
            nextCount = currentCount
            print('\n', currentCount, nextCount)


root = Node(2)
root.left = Node(1)
root.right = Node(3)

levelOrderPrint2(root)
