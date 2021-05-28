from pip._vendor.msgpack.fallback import xrange


class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    for i in xrange(n - 1):
        if not right_pointer.nextNode:
            raise LookupError('Error: n is larger than the linked list.')
        right_pointer = right_pointer.nextNode
    while right_pointer.nextNode:
        left_pointer = left_pointer.nextNode
        right_pointer = right_pointer.nextNode
    return left_pointer


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.nextNode = b
    b.nextNode = c
    c.nextNode = d
    d.nextNode = e

    print(nth_to_last_node(2, a).value)  # the second to last node
