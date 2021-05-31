class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # dictionary

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[
            neighbor] = weight  # nbr= neighbor as the key and weight as a value of the connectedTo dictionary

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:  # dictionary keys
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, fromVertex, toVertex, cost=0):
        if fromVertex not in self.vertList:
            nv = self.addVertex(fromVertex)
        if toVertex not in self.vertList:
            nv = self.addVertex(toVertex)
        self.vertList[fromVertex].addNeighbor(self.vertList[toVertex], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):  # iteration
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
g.addEdge(0, 1, 2)  # from Vertex 0 to Vertex 1 weight= 2

for vertex in g: # take advantages of __contains__ and __iter__
    print(vertex)
    print(vertex.getConnections())
    print('\n')
