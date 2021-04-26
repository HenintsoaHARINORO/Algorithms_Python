class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def reverse(head):
    current = head
    previous = None
    next = None
    while current:
        next = current.nextNode
        current.nextNode = previous

        previous = current
        current = next
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
