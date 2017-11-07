
class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    return self.items.pop(0)

  def is_empty(self):
    return len(self.items) is 0


def breadth_first(graph, source):
  bs_info = []
  queue = Queue()

  for idx in range(0, len(graph)):
    bs_info.append({ "distance": None, "prev": None })

  bs_info[source]["distance"] = 0

  queue.enqueue(source)

  while not queue.is_empty():
    curr = queue.dequeue()

    for i in range(0, len(adj_list[curr])):
      node = adj_list[curr][i]
      if bs_info[node]["prev"] is None and node is not source:
        bs_info[node]["prev"] = curr
        queue.enqueue(node)

    prev = bs_info[curr]["prev"]
    bs_info[curr]["distance"] = 0 if prev is None else bs_info[prev]["distance"] + 1

  print bs_info

adj_list = [
  [1],
  [0, 4, 5],
  [3, 4, 5],
  [2, 6],
  [1, 2],
  [1, 2, 6],
  [3, 5],
  []
]

breadth_first(adj_list, 3)


