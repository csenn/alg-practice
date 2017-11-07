
# add_child(word, index)
# first get parent node and index of part of word to be inserted
# letter at word[index]
# if root node
  # add whole word
# else
  # see how much the 2 match
  # if old word is bigger then the new word
    # existing node needs to be split smaller
  # else
    # the postfix of the new word needs to be added as a child

def get_match_len(a, b):
  loop = min(len(a), len(b))
  match = 0
  for i in range(loop):
    if a[i] != b[i]:
      break
    match += 1
  return match

class TrieNode:
  def __init__(self, prefix=''):
    self.label = prefix[0] if prefix != '' else ''
    self.prefix = prefix
    self.children = []

  def find_insert_location(self, node, word, index, prev_index = 0):
    letter = word[index]
    rest_word = word[index:]

    child = node.find_child(letter)

    if child == None:
      return node, prev_index

    if len(child.prefix) > len(rest_word):
      return child, index

    for i in range(len(child.prefix)):
      if i > len(child.prefix) - 1 or rest_word[i] != child.prefix[i]:
        return child, index
    else:
      return self.find_insert_location(child, word, index + i + 1, index)

  def add_child(self, word, index):
    node, start_index = self.find_insert_location(self, word, index)
    next_word = word[start_index:]

    # print node.prefix, len(node.children), start_index, next_word

    if node == self:
      self.children.append(TrieNode(next_word))
      return

    parent_word = node.prefix
    match = get_match_len(parent_word, next_word)

    parent_word_prefix = parent_word[:match]
    parent_word_suffix = parent_word[match:]
    new_word_suffix = next_word[match:]

    # print len(parent_word) > len(next_word), parent_word, next_word, match

    # For aabb > aa
    if len(parent_word) > len(next_word):
      next_node = TrieNode(parent_word_suffix)
      next_node.children = node.children
      node.prefix = parent_word_prefix
      node.children = [next_node]

      if match < len(next_word):
        node.children.append(TrieNode(new_word_suffix))

    # For aan < aabb or aa == aa
    else:
      # 2 < len(aan)
      if match < len(parent_word):
        next_node = TrieNode(old_word_suffix)
        next_node.children = node.children
        node.prefix = old_word_prefix
        node.children = [next_node]

      node.children.append(TrieNode(new_word_suffix))

  def find_child(self, letter):
    for node in self.children:
      if node.label == letter:
        return node
    return None

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    self.root.add_child(word, 0)

t = Trie()

# keys = ["the","a","there","anaswe","any", "by","their", "bye", "flaw"]

# keys = ["three", "the", "thor"]
# keys = ["there", "the"]
# keys = ["there", "then"]
# keys = ["there", "thor"]

# keys = ["there", "thor", "then"]
# keys = ["there", "then", "thor"]
# keys = ["th", "then"]


# keys = ["there", "the"]

# keys = ["there", "then", "thor"]
# keys = ["there", "then"]
# keys = ["the", "thor"]

# keys = [ "aa","aabb"]
# keys = [ "aa","aabb", "aabbcc"]
# keys = [ "aa","aabb", "aabbcc", "aabbccdd"]

# keys = ["aabbcc", "aabb"]
# keys = ["aabbcc", "aabb",  "aa"]
# keys = ["aabbcc", "aabb", "aa", "aabbccdd"]

# keys = ["sell", "stock"]
# keys = ["sell", "stock", "stop"]
keys = ["bear", "bell", "bid", "bull", "buy", "sell", "stock", "stop"]

for key in keys:
  print '-', key
  t.insert(key)

def print_node(node, level):
  print ' ' * level, node.label, node.prefix
  for child in node.children:
    print_node(child, level + 1)
print_node(t.root, 0)

