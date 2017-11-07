"""
Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot?
"""

def go(n):
    matrix = []
    for i in range(n):
        matrix.append([0 for i in range(n)])

    result = {'val': 0}

    def recurse(i, j):
        next_i = i + 1
        next_j = j + 1

        if next_i < n:
            recurse(next_i, j)
        if next_j < n:
            recurse(i, next_j)

        if next_i == next_j and next_i == n:
            result['val'] += 1

    recurse(0, 0)
    print result['val']

go(3)