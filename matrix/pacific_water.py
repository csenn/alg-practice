from collections import defaultdict

def flow(matrix):
    m = len(matrix)
    n = len(matrix[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
    cache = defaultdict(dict)

    def search(i, j, temp, ocean):
        if (i, j) in temp:
            return

        temp[(i, j)] = True

        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n or matrix[next_i][next_j] < matrix[i][j]:
                continue
            cache[(next_i, next_j)][ocean] = True
            search(next_i, next_j, temp, ocean)

    for i in range(m):
        print i, 0, 'aa', i, n-1
        search(i, 0, {}, 'pacific')
        search(i, n-1, {}, 'atlantic')

    for j in range(n):
        print 0, j, 'bb', m-1, j
        search(0, j, {}, 'pacific')
        search(m-1, j, {}, 'atlantic')

    result = []
    for k, v in cache.iteritems():
        if 'atlantic' in v and 'pacific' in v:
            result.append(k)

    return result

matrix = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]

print flow(matrix)