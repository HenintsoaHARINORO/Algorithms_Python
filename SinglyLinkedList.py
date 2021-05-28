class Node(object):
    def __init__(self,value):
        self.value =value
        self.nextnode = None

if __name__=="__main__":
    a=Node(1)
    b = Node(2)
    c = Node(1)
    a.nextnode = b
    b.nextnode = c

    print(a.value)
    print(a.nextnode.value)