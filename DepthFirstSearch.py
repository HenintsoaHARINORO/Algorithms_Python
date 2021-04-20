class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None