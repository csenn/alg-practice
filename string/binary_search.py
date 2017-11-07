
def binary_search(arr, num, low, high):
    if high == low:
        return high

    mid = low + ((high - low) / 2)

    if arr[mid] == num:
        return mid
    elif arr[mid] > num:
        return binary_search(arr, num, low, mid-1)
    else:
        return binary_search(arr, num, mid + 1, high)

a = []
for idx in range(0, 100):
  a.append(idx)

print binary_search(a, 38, 0, len(a) - 1)
