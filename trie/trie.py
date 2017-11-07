
class Node:
    def __init__(self, letter=''):
        self.letter = letter
        self.children = {}
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.root = Node()

    def find(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return None
            node = node.children[word[i]]
        return node if node.is_leaf else None

    def add(self, word):
        if not word:
            return
        node = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter in node.children:
                node = node.children[letter]
            else:
                node.children[letter] = Node(letter)
                node = node.children[letter]
        node.is_leaf = True

    def remove(self, word):
        node = self.root
        path = [node]
        for i in range(len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            path.append(node)

        # last node in path must be a leaf node
        if not path[-1].is_leaf:
            return False

        # work back through path deleting nodes until reach another leaf
        i = len(path) - 2
        while i > 0:
            del path[i].children[path[i+1].letter]
            if path[i].is_leaf:
                break
            i -= 1

        return True