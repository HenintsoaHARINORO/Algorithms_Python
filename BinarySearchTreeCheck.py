class Node:
    def __init__(self,k,val):
        self.key = k
        self.value= val
        self.left = None
        self.right = None
    def tree_max(node):
        if not node:
            return float("-inf")
        maxleft = tree_max(node.left)
        maxright = tree_max(node.right)
        return max(node.key,maxleft,maxright)

    def tree_min(node):
        if not node:
            return float("inf")
        minleft = tree_min(node.left)
        minright = tree_min(node.right)
        return min(node.key, minleft, minright)