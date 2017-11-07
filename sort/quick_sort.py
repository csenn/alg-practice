import math

"""
[4,2,]98,32,1,2,5,45,6,1, 5, 8,9
2 iteraions and less = 2, idx = 2

4,2,[98],32,1,2,5,45,6,1, 5, 8,9
98 is bigger so less = 2, idx=3

4,2,98,[32],1,2,5,45,6,1, 5, 8,9
32 is bigger so less = 2, idx=4

4,2,98,32,[1],2,5,45,6,1, 5, 8,9
1 is smaller so less = 3, idx=5 and swap
4,2,[1],32,[98],2,5,45,6,1, 5, 8,9

4,2,1,32,98,[2],5,45,6,1, 5, 8,9


"""

def swap(arr, a_index, b_index):
  temp = arr[a_index]
  arr[a_index] = arr[b_index]
  arr[b_index] = temp

def quick_sort(arr):

  def sort(low, high):

    if high - low < 1:
      return

    pivot = arr[high]
    less = low

    # less is always one position past the arr that is lower

    for idx in range(low, high):
      if arr[idx] < pivot:
        swap(arr, less, idx)
        less += 1

    arr[high] = arr[less]
    arr[less] = pivot

    sort(low, less - 1)
    sort(less + 1, high)

  sort(0, len(arr) - 1)
  return arr

if __name__ == '__main__':
  a = [4,2,98,32,1,2,5,45,6,1, 5, 8,9]
  quick_sort(a)
  print a