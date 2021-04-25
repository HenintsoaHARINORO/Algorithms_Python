class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.previousNode = None
        self.nextNode = None


if __name__ == "__main__":
    a = DoublyLinkedListNode(1)
    b = DoublyLinkedListNode(2)
    c = DoublyLinkedListNode(3)

    b.previousNode = a
    a.nextNode = b
    b.nextNode = c
    c.previousNode = b
