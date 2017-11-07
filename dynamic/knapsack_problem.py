# knapsack_problem.py

counters = {
    'a': 0,
    'b': 0,
    'c': 0
}

def knap_sack(nodes, max_weight, top_index):
    counters['a'] += 1
    if top_index == -1 or max_weight <= 0:
        return 0

    n_val, n_weight = nodes[top_index]

    if n_weight > max_weight:
        return knap_sack(nodes, max_weight, top_index-1)

    return max(
        n_val + knap_sack(nodes, max_weight - n_weight, top_index-1),
        knap_sack(nodes, max_weight, top_index-1)
    )

def knap_sack_memoize(nodes, max_weight, top_index, lookup):
    counters['b'] += 1
    if (top_index, max_weight) in lookup:
        return lookup[(top_index, max_weight)]

    if top_index == -1 or max_weight <= 0:
        return 0


    if nodes[top_index][1] > max_weight:
        val = knap_sack_memoize(nodes, max_weight, top_index-1, lookup)
    else:
        val = max(
            nodes[top_index][0] + knap_sack_memoize(nodes, max_weight - nodes[top_index][1], top_index-1, lookup),
            knap_sack_memoize(nodes, max_weight, top_index-1, lookup)
        )

    lookup[(top_index, max_weight)] = val
    return val


"""
        0  1  2  3  4  5  6

(3, 2)  0  0  3  3  3  3  3
(6, 4)  0  0  3  3  6  6  9

(6, 4)  0  0  0  0  6  6  6
(3, 2)  0  0  3  3  6  6  9
"""
def knap_sack_tabular(nodes, max_weight):
    node_len = len(nodes)
    matrix = [[0 for _ in range(max_weight + 1)] for _ in range(node_len)]

    for n, node in enumerate(nodes):
        for w in range(1, max_weight + 1):
            counters['c'] += 1
            n_val, n_weight = node
            if n == 0:
                 matrix[n][w] = 0 if n_weight > w else n_val
            elif n_weight > w:
                matrix[n][w] = matrix[n-1][w]
            else:
                matrix[n][w] = max(
                    matrix[n-1][w],
                    n_val + matrix[n-1][w-n_weight]
                )

    # for row in matrix:
    #     print row

    return matrix[node_len-1][max_weight]


nodes = [
    (210, 45),
    (60, 10),
    (120, 30),
    (100, 20),
    (70, 30),
    (70, 10),
    (20, 40),
    (100, 10),
    (70, 40),
    (80, 20),
    (150, 25),
    (280, 35),
    (100, 10),
    (70, 40),
    (80, 20),
    (150, 25),
    (280, 35),
]
# max_weight = 21
max_weight = 200

# nodes = [
#     (6, 4),
#     (10, 6),
#     (3, 2),
#     (17, 10),
#     (8, 8),
# ]
# max_weight = 6

print knap_sack(nodes, max_weight, len(nodes) - 1)
print knap_sack_memoize(nodes, max_weight, len(nodes) - 1, {})
print knap_sack_tabular(nodes, max_weight)
print counters
