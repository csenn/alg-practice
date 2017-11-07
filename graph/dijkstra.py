
# Simple priority queue
class PriorityQueue:
    def __init__(self):
        self.vals = []

    def add(self, val, weight):
        tup = (val, weight)
        for i in range(len(self.vals)):
            if weight < self.vals[i][1]:
                self.vals.insert(i, tup)
                break
        else:
            self.vals.append(tup)

    def deque(self):
        return self.vals.pop(0)

    def is_empty(self):
        return len(self.vals) == 0


def find(graph, source, dest):
    queue = PriorityQueue()
    queue.add(source, 0)
    while not queue.is_empty():
        node, cost = queue.deque()
        if node == dest:
            print 'Min Steps:', cost
            break
        for child_node, child_cost in graph[node]:
            queue.add(child_node, cost + child_cost)

data = [
    (0, 2, 10),
    (0, 3, 10),
    (0, 4, 10),
    (0, 5, 4),
    (1, 3, 10),

    # shortest path should be 5
    (0, 1, 1),
    (1, 2, 1),
    (2, 3, 1),
    (3, 4, 1),
    (4, 5, 1),

    (1, 4, 20),
    (2, 5, 20)
]

graph = [[] for i in range(6)]

for x, y, weight in data:
    graph[x].append((y, weight))
    graph[y].append((x, weight))

find(graph, 0, 5)
