def has_cycle(head):
    if not head:
        return False

    def iterate(node):
        return node.next if node else None

    a = head
    b = head
    while True:
        a = iterate(a)
        b = iterate(iterate(b))
        if not a:
            return False
        if a == b:
            return True