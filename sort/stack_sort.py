# 5 4 1 2

"""
s = 5 4 1
r = []
el = 2

s = 5 4
r = 2
el = 1

s = 5 4 2

"""

class Stack:
    def __init__(self, items):
        self.items = items

    def add(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

def stack_sort(arr):
    stack = Stack(list(arr))
    stack2 = Stack([])

    while not stack.is_empty():
        el = stack.pop()
        while not stack2.is_empty() and el < stack2.peek():
            stack.add(stack2.pop())
        stack2.add(el)
    return stack2.items


