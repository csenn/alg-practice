import unittest
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from stack_sort import stack_sort
from temp_sort_2 import *

lists = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [1, 6, 3, 4, 5, 2, 1, 2],
    [9, 9, 9, 9, 1, 1, 1, 1],
    [6, 2, 3, 8, 5, 4, 2, 1, 6]
]

def get_results():
    return [(list(l), sorted(l)) for l in lists]

def compare(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

def run(assertEqual, func):
    results = get_results()
    for result in results:
        s = func(result[0])
        assertEqual(True, compare(s, result[1]))

class TestSort(unittest.TestCase):

    def test_selection_sort(self):
        run(self.assertEqual, selection_sort)

    def test_insertion_sort(self):
        run(self.assertEqual, insertion_sort)

    def test_bubble_sort(self):
        run(self.assertEqual, bubble_sort)

    def test_merge_sort(self):
        run(self.assertEqual, merge_sort)

    def test_quick_sort(self):
        run(self.assertEqual, quick_sort)

    def test_heap_sort(self):
        run(self.assertEqual, heap_sort)

    def test_stack_sort(self):
        run(self.assertEqual, stack_sort)

    def test_temp(self):
        run(self.assertEqual, temp_selection_sort)
        run(self.assertEqual, temp_insertion_sort)
        run(self.assertEqual, temp_merge_sort)
        run(self.assertEqual, temp_quick_sort)

if __name__ == '__main__':
    unittest.main()