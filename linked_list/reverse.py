class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

    def set_next(self, node):
        self.next = node

# 1 2 3 4
# 4 3 2 1

def reverse(node):
    if not node.next:
        return node
    next_node = node.next
    node.next = None
    last = reverse(next_node)
    next_node.next = node
    return last

def reverse_stack(node):
    stack = []
    while node:
        stack.append(node)
        temp = node.next
        node.next = None
        node = temp

    start = stack.pop()
    curr = start
    while len(stack):
        curr.next = stack.pop()
        curr = curr.next

    return start

def print_path(node):
    string = ''
    while node:
        print node.val
        string += node.val
        node = node.next
    return string

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.set_next(b)
b.set_next(c)
c.set_next(d)
d.set_next(e)

print print_path(a)
# reverse(a)
# print print_path(reverse(a))
print print_path(reverse_stack(a))