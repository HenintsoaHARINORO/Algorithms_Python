from collections import OrderedDict
from enum import Enum


class State(Enum):
    unvisited = 1  # white
    visited = 2  # black
    visiting = 3  # gray


class Node:
    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # neighbors ,OrderDict is a dict that remembers the order that keys were first inserted

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
