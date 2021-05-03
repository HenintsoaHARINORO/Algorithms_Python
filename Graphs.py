from collections import OrderedDict
from enum import Enum


class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3


class Node:
    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # neighbors

    def __str__(self):
        return str(self.num)


class Graph:
    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight


g = Graph()
g.add_edge(0, 1, 5)
print(g.nodes)
