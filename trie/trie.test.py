import unittest
from trie import Trie

words = ["the","a","there","anaswe","any", "by","their", "bye", "flaw", "cool"]

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        for word in words:
            self.trie.add(word)

    def test_words_added(self):
        for word in words:
            self.assertEqual(self.trie.find(word).letter, word[-1])

    def test_words_dont_exist(self):
        # should not find words that dont exist
        self.assertEqual(self.trie.find('x'), None)
        self.assertEqual(self.trie.find('theiro'), None)
        # should not find partials
        self.assertEqual(self.trie.find('t'), None)

    def test_remove_word(self):
        # should remove
        self.assertEqual(self.trie.remove('their'), True)
        self.assertEqual(self.trie.find('the').letter, 'e')
        # should remove word
        self.assertEqual(self.trie.remove('bye'), True)
        self.assertEqual(self.trie.find('bye'), None)
        self.assertEqual(self.trie.remove('bye'), False)
        self.assertEqual(self.trie.find('by').letter, 'y')
        # dont remove non-existant
        self.assertEqual(self.trie.remove('fish'), False)
         # dont remove partial
        self.assertEqual(self.trie.remove('co'), False)


if __name__ == '__main__':
    unittest.main()