class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.head or not self.head.next:
            return None

        self.head = self.head.next

if __name__ == '__main__':
    stack = Stack()

    stack.add(1)
    print stack.head.data
    stack.add(2)
    print stack.head.data
    stack.pop()
    print stack.head.data
    stack.add(4)
    print stack.head.data


