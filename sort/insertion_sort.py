"""
 Loop through array
 At each index move backwards and to find number smaller then current
 if not smaller, then swap them
"""

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def insertion_sort(arr):
    for idx in range(0, len(arr)):
        current = idx
        while current > 0 and arr[current - 1] > arr[current]:
            swap(arr, current-1, current)
            current -= 1
    return arr

if __name__ == '__main__':
    a = [4,2,6,98,32,1,2,5,45,6,1, 5, 8,9]
    insertion_sort(a)
    print a