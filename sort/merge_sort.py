import math

def merge_sort(arr):

  def merge(low, midpoint, high):

    first_index = low
    second_index = midpoint + 1

    first_set = []
    second_set = []

    for idx in range(low, high + 1):
      if idx <= midpoint:
        first_set.append(arr[idx])
      else:
        second_set.append(arr[idx])

    first_index = 0
    second_index = 0
    counter = low

    while True:
      is_first_done = first_index > len(first_set) - 1
      is_second_done = second_index > len(second_set) - 1

      if is_first_done and is_second_done:
        break

      elif is_first_done:
        arr[counter] = second_set[second_index]
        second_index += 1

      elif is_second_done:
        arr[counter] = first_set[first_index]
        first_index += 1

      elif  first_set[first_index] < second_set[second_index]:
        arr[counter] = first_set[first_index]
        first_index += 1

      else:
        arr[counter] = second_set[second_index]
        second_index += 1

      counter += 1

  def sort(low, high):

    if high - low < 1:
      return

    midpoint = int(math.floor((low + high) / 2))

    sort(low, midpoint)
    sort(midpoint + 1, high)
    merge(low, midpoint, high)

  sort(0, len(arr) - 1)

  return arr


if __name__ == '__main__':
  a = [4,2,6,98,32,1,2,5,45,6,1, 5, 8,9]

  merge_sort(a)

  print a