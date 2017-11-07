
"""
1 1 1
0 0 0
0 0 0

0 0 1
0 0 1
0 0 1


1 0 0
1 0 0
1 0 0


i = 0, j = 0
i = 0, j = 2

i = 0, j = 1
i = 1, j = 2

i = 0, j = 2
i = 2, j = 2

i = 1, j = 0
i = 0, j = 1

i = 2, j = 0
i = 0, j = 0


i  j  i_  j_
0  0  0   2
0  1  1   2
0  2  2   2
1  0  0   1
2  0  0   0


"""

def swap(matrix, i, j, i_, j_):
  temp = matrix[i][j]
  matrix[i][j] = matrix[i_][j_]
  matrix[i_][j_] = temp

next_matrix = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

def rotate(matrix):
  matrix_len = len(matrix)
  n = matrix_len - 1
  for i in range(matrix_len / 2):
    j_ = n-i
    for j in range(matrix_len / 2):
      # next_matrix[j][j_] = matrix[i][j]
      #print i, j, j, j_
      swap(matrix, i, j, j, j_)

matrix = [
  [1, 1, 1],
  [0, 0, 0],
  [0, 0, 0]
]

# works, but needs another matrix. Can be done without
# another matrix
rotate(matrix)
print next_matrix

print matrix







