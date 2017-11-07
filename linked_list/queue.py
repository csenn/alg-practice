class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            node.next.prev = node
        else:
            self.tail = node
        self.head = node

    def dequeue(self):
        if self.tail:
            temp = self.tail
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None
            return temp

    def print_me(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(node.data)
            node = node.next
        print ' '.join(map(str, nodes))


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.print_me()
    q.enqueue(2)
    q.print_me()
    q.enqueue(3)
    q.print_me()
    print 'deqeue', q.dequeue().data
    q.print_me()
    print 'deqeue', q.dequeue().data
    q.enqueue(5)
    q.print_me()
    q.enqueue(7)
    q.print_me()
    print 'deqeue', q.dequeue().data
    q.print_me()
