# builds a simple tree using a dict


class Node:
  def __init__(self, label):
    self.children = {}
    self.out = []

def build_tree(patterns):
  root = Node('-1')

  for pattern in patterns:
    node = root
    for letter in pattern:
      node = node.children.setdefault(letter, Node(letter))
    node.out.append(pattern)

  return root

patterns = ['heat', 'hear', 'ear']
tree = build_tree(patterns)