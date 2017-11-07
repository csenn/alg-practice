"""
Lets see if I can approach thinking about this differently

0 1 2 3 4 5 6 7 8

7 8 0 1 2 3 4 5 6

3 4 5 6 7 8 0 1 2

"""

def recurse(arr, target, low, high):
    if high - low < 0:
        return -1

    midpoint = low + (high - low) / 2

    if arr[midpoint] == target:
        return midpoint

    if arr[midpoint] > arr[high]:
        if target >= arr[low] and target < arr[midpoint]:
            return recurse(arr, target, low, midpoint - 1)
        return recurse(arr, target, midpoint + 1, high)

        # 8 0 1 where target == 1
        # if target < arr[midpoint] and target <= arr[high]:
        #     return recurse(arr, target, midpoint + 1, high)
        # # 7 8 1 where target == 8
        # elif target > arr[midpoint] and target >= arr[high]:
        #     return recurse(arr, target, midpoint + 1, high)
        # return recurse(arr, target, low, midpoint - 1)
    else:
        if target > arr[midpoint] and target <= arr[high]:
            return recurse(arr, target, midpoint + 1, high)
        else:
            return recurse(arr, target, low, midpoint - 1)

tests = [
    (0, 0, [0, 1, 2, 3, 4, 5, 6, 7, 8]),
    (8, 8, [0, 1, 2, 3, 4, 5, 6, 7, 8]),
    (0, 2, [7, 8, 0, 1, 2, 3, 4, 5, 6]),
    (8, 1, [7, 8, 0, 1, 2, 3, 4, 5, 6]),
    (0, 6, [3, 4, 5, 6, 7, 8, 0, 1, 2]),
    (8, 5, [3, 4, 5, 6, 7, 8, 0, 1, 2]),
]

for x, ans, arr in tests:
    print 'ans', ans, recurse(arr, x, 0, len(arr) - 1)

# arr = [4, 5, 6, 7, 0, 1, 2]
# arr = [5, 1, 3]
# arr = [4,5,6,7,8,1,2,3]
# print recurse(arr, 8, 0, len(arr) - 1)