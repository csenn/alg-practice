
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def get_height(self):
        return self._get_max_height(self.root) + 1

    def is_balanced(self):
        return 1 >= self._get_max_height(self.root) - self._get_min_height(self.root)

    @staticmethod
    def _get_max_height(node):
        if not node:
            return -1
        return 1 + max(BST._get_max_height(node.left), BST._get_max_height(node.right))

    @staticmethod
    def _get_min_height(node):
        if not node:
            return -1
        return 1 + min(BST._get_min_height(node.left), BST._get_min_height(node.right))


    def search(self, num):
        current = self.root
        while True:
            if current.data == num:
                return current
            if num < current.data:
                if not current.left:
                    return None
                current = current.left
            else:
                if not current.right:
                    return None
                current = current.right

    def add_node(self, num):
        if not self.root:
            self.root = Node(num)
            return

        current = self.root
        while True:
            if num == current.data:
                break
            if num < current.data:
                if not current.left:
                    current.left = Node(num)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = Node(num)
                    break
                current = current.right

    def remove_node(self, num):
        self.root = BST._remove_node(self.root, num)

    @staticmethod
    def _remove_node(node, num):
        if not node:
            return None

        if num < node.data:
            node.left = BST._remove_node(node.left, num)
        elif num > node.data:
            node.right = BST._remove_node(node.right, num)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                lowest_right_node = node.right
                while lowest_right_node.left:
                    lowest_right_node = lowest_right_node.left

                node.data = lowest_right_node.data
                node.right = BST._remove_node(node.right, lowest_right_node.data)
        return node

    def get_in_order_str(self):
        self.in_order_str = ''
        self._build_in_order_str(self.root)
        return self.in_order_str[:-1]

    def _build_in_order_str(self, node):
        if not node:
            return
        self._build_in_order_str(node.left)
        self.in_order_str += str(node.data) + ' '
        self._build_in_order_str(node.right)

    @staticmethod
    def print_tree(node, level=0):

        return

        levels = []
        def recurse(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node or None)
            if node:
                recurse(node and node.left or None, level + 1)
                recurse(node and node.right or None, level + 1)

        recurse(node, level)
        for level_arr in levels:
            string = ''
            for node in level_arr:
                string += str(node and node.data or '-1') + ' '
            print string

