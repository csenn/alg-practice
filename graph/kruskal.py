# finds minimum spanning trees
# uses disjoint_set data structure
# seperates nodes into sets

parent = dict()

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

# could add rank optimization
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    parent[root_b] = root_a

def kruskals(n, init_edges):
    for i in range(n):
        parent[i] = i

    edges = sorted(init_edges, key=lambda tup: tup[2])

    # will choose smallest edges until there are no cycles
    min_tree = []
    for edge in edges:
        if find(edge[0]) == find(edge[1]):
            continue
        union(edge[0], edge[1])
        min_tree.append(edge)

    return min_tree

data = [
    (0, 2, 10),
    (0, 3, 10),
    (0, 4, 10),
    (0, 5, 10),
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

print kruskals(6, data)