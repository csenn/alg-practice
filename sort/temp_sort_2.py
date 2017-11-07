
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

"""
find smallest in rest of array
and then swap it
"""
def temp_selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        smallest = i
        for j in range(i+1, arr_len):
            if arr[j] < arr[smallest]:
                smallest = j
        if i != smallest:
            swap(arr, i, smallest)
    return arr


"""
Go forward and then work backwards
3, 2, 1, 4
"""
def temp_insertion_sort(arr):
    arr_len = len(arr)
    for i in range(1, arr_len):
        for j in range(i, 0, -1):
            if arr[j-1] < arr[j]:
                break
            swap(arr, j, j-1)
    return arr

"""
    split at midpoint, and then
    recombine
"""
def temp_merge_sort(arr):
    def merge(low, midpoint, high):
        low_arr = []
        high_arr = []
        for i in range(low, high + 1):
            if i <= midpoint:
                low_arr.append(arr[i])
            else:
                high_arr.append(arr[i])

        low_len, high_len = len(low_arr), len(high_arr)
        i, j, k = 0, 0, low
        while i < low_len or j < high_len:
            if i == low_len:
                val = high_arr[j]
                j += 1
            elif j == high_len:
                val = low_arr[i]
                i += 1
            elif low_arr[i] < high_arr[j]:
                val = low_arr[i]
                i += 1
            else:
                val = high_arr[j]
                j += 1
            arr[k] = val
            k += 1

    def sort(low, high):
        if high - low == 0:
            return
        midpoint = low + (high-low) / 2
        sort(low, midpoint)
        sort(midpoint + 1, high)
        merge(low, midpoint, high)
    sort(0, len(arr) - 1)
    return arr

"""
take last element in array
move everything smaller to left and greater to right
repeat in range
5, 4, 1, 2

1, 5, 4, 2
1, 2, 4, 5

low = 0, i = 0

"""
def temp_quick_sort(arr):
    def sort(low, high):
        if high - low < 0:
            return
        l_index, pivot = low, high
        for i in range(low, high):
            if arr[i] < arr[pivot]:
                swap(arr, i, l_index)
                l_index += 1
        swap(arr, l_index, pivot)
        sort(low, l_index - 1)
        sort(l_index + 1, high)
    sort(0, len(arr) - 1)
    return arr

if __name__ == '__main__':
    temp_quick_sort([5, 4, 1, 2, 3])
