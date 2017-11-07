def traverse(matrix, start, end):
    matrix_len = len(matrix)
    distance = [0 for _ in range(matrix_len)]
    parent = [None for _ in range(matrix_len)]

    q = [start]
    while len(q):
        current = q.pop(0)
        if current == end:
            return distance[current]

        for i, val in enumerate(matrix[current]):
            if val == 1 and not parent[i] and  i != start:
                parent[i] = current
                distance[i] = distance[current] + 1
                q.append(i)

    return None


"""
1 - 3
3 - 2
2 - 4
"""
matrix = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
]

print traverse(matrix, 0, 3)