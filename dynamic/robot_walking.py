def robot_walking(m, n):
    m = m - 1
    n = n - 1
    def recurse(i, j):
        if i == m and j == n:
            return 1

        a = recurse(i + 1, j) if i < m else 0
        b = recurse(i, j + 1) if j < n else 0
        return a + b

    return recurse(0, 0)

def robot_walking_memoize(m, n):
    m = m - 1
    n = n - 1
    cache = {}
    def recurse(i, j):
        if (i, j) in cache:
            return cache[(i, j)]

        if i == m and j==n:
            cache[(i, j)] = 1
        else:
            val = 0
            if i < m:
                val += recurse(i + 1, j)
            if j < n:
                val += recurse(i, j + 1)
            cache[(i, j)] = val

        return cache[(i, j)]

    return recurse(0, 0)

def robot_walking_matrix(m, n):
    m = m - 1
    n = n - 1
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    matrix[m][n] = 1

    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i - 1 >= 0:
                matrix[i-1][j] += matrix[i][j]
            if j - 1 >= 0:
                matrix[i][j-1] += matrix[i][j]
    return matrix[0][0]

print robot_walking(6, 5)
print robot_walking_memoize(6, 5)
print robot_walking_matrix(6, 5)