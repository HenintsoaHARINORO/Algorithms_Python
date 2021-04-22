import sys

class Node(object):
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = []
        self.minDistance = sys.maxsize
class Edge(object):
    def __init__(self,weight,startVertex,targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
class BellmanFord(object):
    HAS_CYCLE = False
    def calculateShortestPath(self,vertexList,edgeList,startVertex):
        startVertex.minDistance = 0
        for i in range(0,len(vertexList)-1):
            for edge in edgeList:
                u =edge.startVertex
                v= edge.targetVertex
                newDistance= u.minDistance + edge.weight
                if newDistance <v.minDistance:
                    v.minDistance=newDistance
                    v.predecessor = u
        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected")
                BellmanFord.HAS_CYCLE = True
                return
    def hasCycle(self,edge):
        if(edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
            return  True
        else:
            return False
    def getShortestPath(self,targetVertex):
        if not BellmanFord.HAS_CYCLE:
            print("Shortest path with value",targetVertex.minDistance)
            node = targetVertex
            while node is not None:
                node = node.predecessor
        else:
            print("Negative cycle detected")
