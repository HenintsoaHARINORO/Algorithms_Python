class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class DepthFirstSearch(object):
    def dfs(self,node):
        node.visited = True
        print("%s" % node.name)

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)


node1 = Node("A")
node2 = Node("H")
node3 = Node("C")
node4 = Node("E")
node5 = Node("1")
node6 = Node("4")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node2.adjacencyList.append(node5)
node3.adjacencyList.append(node6)
dfs = DepthFirstSearch()
dfs.dfs(node1)