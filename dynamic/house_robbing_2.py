# houses are in a circle now
"""
5, 1, 2, 3, 4

     5
  4     1
    3  2
"""
def rob_recurse(nums):
    num_len = len(nums)

    cache = {}
    def recurse(i, high):
        if (i, high) in cache:
            return cache[(i, high)]

        if i > high:
            cache[(i, high)] = 0
        else:

            cache[(i, high)] = max(
                nums[i] + recurse(i + 2, high),
                recurse(i + 1, high)
            )
        return cache[(i, high)]

    high = num_len - 1
    return max(recurse(0, high-1), recurse(1, high))

arr = [4, 2, 3, 4, 5]

print rob_recurse(arr)