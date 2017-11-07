def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def temp_selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        smallest = i
        for j in range(i+1, arr_len):
            if arr[j] < arr[smallest]:
                smallest = j
        if smallest != i:
            swap(arr, i, smallest)
    return arr

def temp_insertion_sort(arr):
    for i in range(1, len(arr)):
        current = i
        while current > 0 and arr[current] < arr[current-1]:
            swap(arr, current, current-1)
            current -= 1
    return arr

def temp_merge_sort(arr):

    def merge(low, pivot, high):
        left, right = [], []

        for i in range(low, pivot + 1):
            left.append(arr[i])

        for i in range(pivot + 1, high + 1):
            right.append(arr[i])

        i = low
        l_len, r_len = len(left), len(right)
        l, r = 0, 0
        while l < l_len or r < r_len:
            if l == l_len:
                val = right[r]
                r += 1
            elif r == r_len:
                val = left[l]
                l += 1
            elif left[l] < right[r]:
                val = left[l]
                l += 1
            else:
                val = right[r]
                r += 1

            arr[i] = val
            i += 1

    def sort(low, high):
        if high-low == 0:
            return

        pivot = low + (high-low) / 2
        sort(low, pivot)
        sort(pivot + 1, high)
        merge(low, pivot, high)

    sort(0, len(arr) - 1)

    return arr


def temp_quick_sort(arr):

    def sort(low, high):
        if high - low < 1:
            return

        pivot = arr[high]
        low_index = low
        for i in range(low, high):
            if arr[i] <= pivot:
                swap(arr, i, low_index)
                low_index += 1

        swap(arr, low_index, high)
        sort(low, low_index - 1)
        sort(low_index + 1, high)

    sort(0, len(arr) - 1)
    return arr

if __name__ == '__main__':
    print temp_quick_sort([3, 1, 7, 5, 4, 3, 2])


