import pprint

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

class DFS:
  def __init__(self, graph):
    self.graph = graph
    self.info = []
    self.time = 0
    for index in range(len(graph)):
      self.info.append({ "status": "undiscovered", "parent": None, "distance": None,
        "entry_time": None, "exit_time": None, "reachable_ancestor": None })

  def process(self, node, distance=1):
    self.time += 1
    self.info[node]["status"] = "discovered"
    self.info[node]["entry_time"] = self.time
    self.proccess_vertex_early(node)

    for child in self.graph[node]:
      if self.info[child]['status'] == "undiscovered":
        self.process_edge(node, child)
        self.info[child]["parent"] = node
        self.info[child]["distance"] = distance
        self.process(child, distance + 1)

      elif self.info[child]['status'] == 'discovered':
        print 'fisisisi'
        self.process_edge(node, child)

    self.info[node]["status"] = "processed"
    self.time += 1
    self.info[node]["exit_time"] = self.time
    self.process_vertex_late(node)

  def proccess_vertex_early(self, node):
    self.info["reachable_ancestor"] = node
    print 'early: ' + str(node)

  def process_vertex_late(self, node):
    print 'late: ' + str(node)

  def process_edge(self, x, y):
    print str(x) + ', ' + str(y)

dfs = DFS(adj_list)
dfs.process(3)
pprint.pprint(dfs.info)
