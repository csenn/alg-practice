def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if not root:
        return []

    q = deque()
    q.append((0, root))
    result = []
    while len(q):
        curr_level, curr_node = q.popleft()
        while curr_level >= len(result):
            result.append([])

        result[curr_level].append(curr_node.val)

        if curr_node.left:
            q.append((curr_level+1, curr_node.left))

        if curr_node.right:
            q.append((curr_level+1, curr_node.right))

    return result

def levelOrder_2(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if not root:
        return []

    result, level = [], [root]
    while len(level):
        result.append([])
        temp = []
        for node in level:
            result[-1].append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        level = temp

    return result