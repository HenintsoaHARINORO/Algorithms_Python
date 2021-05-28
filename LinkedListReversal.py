class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def reverse(head):
    current = head
    previous = None
    nextNode = None
    while current:
        nextNode = current.nextNode
        current.nextNode = previous

        previous = current
        current = nextNode
    return previous


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.nextNode = b
    b.nextNode = c
    c.nextNode = d

    reverse(a)
    print(d.nextNode.value)
    print(c.nextNode.value)
    print(b.nextNode.value)
