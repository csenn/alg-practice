import unittest

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node(None)

    def add(self, val):
        next_node = Node(val)
        next_node.next = self.head
        self.head = next_node

    def pop(self):
        if self.head.val == None:
            print("Nothing in stack")
            return None

        ret_val = self.head.val
        self.head = self.head.next
        return ret_val

    def peek(self):
        return self.head.val

class TestStack(unittest.TestCase):

    def test_stack(self):

        stack = Stack()
        stack.add(3)
        self.assertEqual(stack.peek(), 3)
        stack.add(7)
        self.assertEqual(stack.peek(), 7)

        self.assertEqual(stack.pop(), 7)
        self.assertEqual(stack.peek(), 3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), None)

if __name__ == '__main__':
    unittest.main()
