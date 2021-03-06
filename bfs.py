class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None


class BreadFirstsearch(object):
    def bfs(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:  # while the queue is not empty
            actualNode = queue.pop(0)  # FIFO
            print("%s" % actualNode.name)

            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)


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

bfs = BreadFirstsearch()
bfs.bfs(node1)
