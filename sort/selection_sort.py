
def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def selection_sort(arr):

  swaps = 0
  iterations = 0

  for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
      iterations += 1
      if arr[min_index] > arr[j]:
        min_index = j

    if min_index != i:
      swap(arr, i, min_index)
      swaps += 1

  # print 'iterations', iterations
  # print 'swaps', swaps
  return arr


# a = [4,5,6,98,32,1,2,5,45,6,1, 5, 8,9]
a = [5, 4, 2, 6, 1, 3]

f = open('temp_data.txt', 'r') #1026
m = f.readline()
a = [int(i) for i in f.readline().strip().split()]

b = list(reversed(a))
selection_sort(a)
selection_sort(b)

# print a