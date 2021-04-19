class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None
class BreadFirstsearch(object):
    def bfs(self,startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:
            actualNode = queue.pop(0) #FIFO
            print("%s" % actualNode.name)

            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited= True
                    queue.append(n)

node1 =Node("A")
node2 =Node("H")
node3 =Node("C")
node4 =Node("1")
node5 =Node("E")
node6 =Node("4")

node1 .adjacencyList.append(node2)
node1 .adjacencyList.append(node3)
node2 .adjacencyList.append(node5)
node2 .adjacencyList.append(node4)
node4 .adjacencyList.append(node6)

bfs =BreadFirstsearch()
bfs.bfs(node1)


