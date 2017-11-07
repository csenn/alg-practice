

def mult_indexes(arr, low, high):
    if low >= len(arr):
        return 0
    result = arr[low]
    for i in range(low + 1, high + 1):
        result *= arr[i]
    return result

def get_best(arr):
    if len(arr) == 0:
        return 0

    neg_indexes = []
    for i, num in enumerate(arr):
        if num < 0:
            neg_indexes.append(i)




    count = len(neg_indexes)

    full_try =  mult_indexes(arr, 0, len(arr) - 1)

    if count == 0 or count % 2 == 0:
        return full_try

    low_try = mult_indexes(arr, neg_indexes[0] + 1, len(arr) - 1)
    high_try = mult_indexes(arr, 0, neg_indexes[-1] - 1)

    return max(low_try, high_try, full_try)


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    results = [[]]
    for num in nums:
        if num == 0:
            results.append([])
            continue
        results[-1].append(num)


    bests = map(get_best, results)

    return max(bests)

print 6, maxProduct([2,3,-2,4])
print 48, maxProduct([2, -1, 3,-2,4])
print 24, maxProduct([2, 0, -1, 3, -2, 4])
print 4, maxProduct([2, 0, -1, 0, 3, -2, 4])
print -2, maxProduct([-2])
print 12, maxProduct([-2, -3, -4])
print 120, maxProduct([-2, -3, -4, -5])

