# longest common subsequence

"""
  H E A T
S 0 0 0 0
H 1 1 1 1
O 1 1 1 1
A 1 1 2 2
T 1 1 2 3
"""

"""
  N O H A R A A A
S 0 0 0 0 0 0 0 0
H 0 0 1 1 1 1 1 1
I 0 0 1 1 1 1 1 1
N 1 1 1 1 1 1 1 1
C
H
A
N
"""

def print_matrix(matrix):
  for row in matrix:
    print row

def lcs(a, b):

  matrix = [[0 for _ in range(len(b))]  for _ in range(len(a))]

  # def recurse(i, j):
  #   if i < 0 or j < 0:
  #     return 0

  #   back_i = recurse(i-1, j)
  #   back_j = recurse(i, j-1)
  #   max_el = max(back_i, back_j)

  #   if a[i] == b[j]:
  #     max_el += 1

  #   matrix[i][j] = max_el

  #   return max_el

  def get_val(i, j):
    if i < 0: return 0
    if j < 0: return 0
    return matrix[i][j]

  for i in range(len(a)):
    for j in range(len(b)):

      if a[i] == b[j]:
        max_el = get_val(i-1, j - 1) + 1
      else:
        back_i = get_val(i-1, j)
        back_j = get_val(i, j-1)
        max_el = max(back_i, back_j)

      matrix[i][j] = max_el

  print_matrix(matrix)
  return max(matrix[len(matrix) - 1])

a = 'heat'
b = 'shoat'

a = 'SHINCHAN'
b = 'NOHARAAA'

print lcs(a, b)