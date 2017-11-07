# Loop backwards through the array
# In first for loop, num will be len(array)
# largest will be the current index
# left will be its child, right will be the other child
# there will not be left or right if the node is
# on the bottom of the binary tree

# if left < num and right < num is really asking if the nodes even exists
# nodes in the lowest or second to lowest layer may not have children
# Find the largest out of the 3 in the triangle

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def heap_sort(arr):


  # This function forces the node at the index to
  # be larger then its two children, and will work
  # its way down through the tree to put that node in
  # its correct location.
  def heapify(num, node_idx):
    largest = node_idx
    left = 2 * node_idx + 1
    right = 2 * node_idx + 2

    if left < num and arr[left] > arr[largest]:
      largest = left

    if right < num and arr[right] > arr[largest]:
      largest = right

    if largest != node_idx:
      swap(arr, node_idx, largest)

      # this recursive call will push a the top node down
      # to where it needs to be
      heapify(num, largest)

  arr_len = len(arr)

  # Create a max heap
  for idx in range(arr_len, -1, -1):
    heapify(arr_len, idx)

  # Sort the max heap
  # The max number will be at the very top
  # So place that number at the last position in the array
  # Then do another heapify, which will get the max number
  # to the top again
  for idx in range(arr_len-1, 0, -1):
    swap(arr, idx, 0)
    heapify(idx, 0)

  return arr

# a = [4, 10, 3, 5, 1]
a = [4,2,6,98,32,1,2,5,45,6,1, 5, 18,9, 16, 18, 67, 21, 18, 23, 78]
# a = [4,2,6,98,32,1,2,5,45,6,1, 5]

15#               04
7 #       02              06
3 #   98      32      01     02
1 # 05  45  06  01  05 34

# 1
# 2
# 3
# 4

# level nodes
# 0 1  1
# 1 2  3
# 2 4  7
# 3 8  15
# 4 16 31
# 5 32 63



def fix_num(num):
  if num < 10:
    return ' ' + str(num)
  else:
    return str(num)

def get_spaces(num):
  text = ''
  for idx in range(0, num):
    text += ' '
  return text

def print_heap(heap):
  num = len(heap)
  level = 0
  nodes = 0
  node_levels = []

  while True:
    nodes += pow(2, level)
    node_levels.append(nodes)
    if nodes > num:
      break
    level += 1

  curr_index = 0
  nodes = 0

  for curr_level in range(0, level + 1):
    nodes += pow(2, curr_level)
    text = ''

    for idx in range(curr_index, nodes):
      if idx < num:
        buff = get_spaces(node_levels[level-curr_level])
        text += buff + fix_num(heap[idx]) + buff
      curr_index += 1

    print text

if __name__ == 'main':

  heap_sort(a)
  print_heap(a)
  print a
