def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr):
    swaps = True
    arr_len = len(arr)
    while swaps != 0:
        swaps = 0
        for i in range(1, arr_len):
            if arr[i-1] > arr[i]:
                swap(arr, i-1, i)
                swaps += 1
    return arr
