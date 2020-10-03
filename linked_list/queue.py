import unittest

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 1 -> 2    -> 3 -> 4
# 1 <- 2 <- 3 <- 4

# 4
# 3 <- 4
# 2 <- 3 <- 4

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def queue(self, val):
        next_node = Node(val)

        if not self.front:
            self.front = next_node
            self.back = next_node
        else:
            self.back.next = next_node
            self.back = next_node

    def dequeue(self):
        if self.front == None:
            return None

        ret_val = self.front.val

        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next

        return ret_val

    def peek(self):
        return self.front.val

class TestQueue(unittest.TestCase):

    def test_stack(self):

        q = Queue()
        q.queue(3)
        self.assertEqual(q.peek(), 3)
        q.queue(7)
        self.assertEqual(q.peek(), 3)
        q.queue(5)
        self.assertEqual(q.peek(), 3)

        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.peek(), 7)

        self.assertEqual(q.dequeue(), 7)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), None)

if __name__ == '__main__':
    unittest.main()
