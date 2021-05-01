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

root  = Node(2)
root.left = Node(1)
root.right = Node(3)


levelOrderPrint(root)