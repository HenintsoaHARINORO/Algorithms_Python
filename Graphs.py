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
        self.adjacent = OrderedDict()

    def __str__(self):
        return str(self.num)
