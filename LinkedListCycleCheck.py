class Node(object):
    def __init__(self,value):
        self.value = value
        self .nextNode =  None
def cycle_check(node):
    marker1 = node
    marker2 = node
    while marker2 != None and marker2.nextNode != None:
        marker1 = marker1.nextNode
        print(marker1.value)
        marker2 = marker2 .nextNode.nextNode

        print(marker2.value)
        if marker2 == marker1:
            return True
    return False

if __name__=="__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextNode = b
    b .nextNode = c
    c .nextNode = a # cycle


    print(cycle_check(c))

