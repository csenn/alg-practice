
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
    queue = Queue()
    distance = [-1] * len(graph)
    state = ['undisovered'] * len(graph)
    parent = [None] * len(graph)

    queue.enqueue(source)
    state[source] = 'discovered'

    while not queue.is_empty():
        curr = queue.dequeue()
        for child in graph[curr]:
            if state[child] == 'undisovered':
                state[child] = 'discovered'
                parent[child] = curr
                queue.enqueue(child)

        if curr == source:
            distance[curr] = 0
        else:
            distance[curr] = distance[parent[curr]] + 1

    print parent
    print distance


if __name__ == '__main__':
    # Should be
    # [4, 3, 1, 0, 2, 2, 1, -1]
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


