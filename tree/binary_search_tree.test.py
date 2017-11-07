import unittest
from binary_search_tree import BST

def build_tree(nodes):
    bst = BST()
    for node in nodes:
        bst.add_node(node)
    return bst


class TestBST(unittest.TestCase):
    def test_add_node(self):
        bst = build_tree([5, 7, 1, 3, 2])
        self.assertEqual(bst.root.data, 5)
        self.assertEqual(bst.root.right.data, 7)
        self.assertEqual(bst.root.left.data, 1)
        self.assertEqual(bst.root.left.right.data, 3)
        self.assertEqual(bst.root.left.right.left.data, 2)

    def test_get_height(self):
        bst_1 = build_tree([2, 3, 4, 5, 6, 1])
        bst_2 = build_tree([2, 1, 3])
        self.assertEqual(bst_1.get_height(), 5)
        self.assertEqual(bst_2.get_height(), 2)

    def test_search(self):
        bst = build_tree([5, 7, 1, 3, 2])
        self.assertEqual(bst.search(5).data, 5)
        self.assertEqual(bst.search(7).data, 7)
        self.assertEqual(bst.search(3).data, 3)
        self.assertEqual(bst.search(4), None)
        self.assertEqual(bst.search(8), None)

    def test_remove_node(self):
        def run(index, arr):
            arr = list(arr)
            bst = build_tree(arr)
            bst.remove_node(arr[index])
            arr.pop(index)
            self.assertEqual(bst.get_in_order_str(), ' '.join(map(str, sorted(arr))))

        arr = [5, 7, 2, 1, 8, 3, 6, 9, 11, 10, 4]
        for i in range(len(arr)):
            run(i, arr)

    def test_in_order(self):
        arrs = [
            [5, 7, 1, 3, 2],
            [9, 8, 7, 6, 5],
            [1, 2, 3, 4, 5]
        ]
        for arr in arrs:
            bst = build_tree(arr)
            string = bst.get_in_order_str()
            self.assertEqual(string, ' '.join(map(str, sorted(arr))))

if __name__ == '__main__':
    unittest.main()