from pip._vendor.urllib3.connectionpool import xrange


class Queue2Stacks(object):
    def __init__(self):
        # Two stacks
        self.in_stack = []  # enqueue operation
        self.out_stack = []  # dequeue

    def enqueue(self, element):
        self.in_stack.append(element)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


if __name__ == "__main__":
    q = Queue2Stacks()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())
