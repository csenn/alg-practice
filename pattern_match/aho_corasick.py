class Node:
  def __init__(self, label):
    self.label = label
    self.children = {}
    self.out = []
    self.fail = None


class Aho:
  def __init__(self):
    self.root = Node('-1')

  def build_tree(self, patterns):
    for pattern in patterns:
      node = self.root
      for letter in pattern:
        node = node.children.setdefault(letter, Node(letter))
      node.out.append(pattern)

  def build_state_machine(self):
    queue = []
    for k, node in self.root.children.iteritems():
      node.fail = self.root
      queue.append(node)

    while len(queue) > 0:
      curr_node = queue.pop(0)
      for key, child_node in curr_node.children.iteritems():
        queue.append(child_node)
        fail_node = curr_node.fail
        print 'eee', fail_node.label, key
        while fail_node != None and not fail_node.children.has_key(key):
          fail_node = fail_node.fail
        child_node.fail = fail_node.children[key] if fail_node else self.root
        child_node.out += child_node.fail.out
        print child_node.out, child_node.fail.out

  def add_patterns(self, patterns):
    self.build_tree(patterns)
    self.build_state_machine()

  def find_matches(self, text):
    node = self.root

    for i in xrange(len(text)):
      while node != None and not node.children.has_key(text[i]):
        node = node.fail
      if node == None:
        node = self.root
        continue
      node = node.children[text[i]]
      for pattern in node.out:
        print "At pos %s found pattern: %s" % (i - len(pattern) + 1, pattern)


patterns = ['he', 'she', 'his', 'her', 'hers']
# patterns = ['hello', 'loan']
text = 'shherishers'

aho = Aho()
aho.add_patterns(patterns)
aho.find_matches(text)