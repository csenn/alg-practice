"""
1: [1]
2: [1, 1], [2]
3: [1, 1, 1], [2, 1], [1, 2], [3]
"""

def recursive(nums, target):
    def recurse(sum_here):
        if sum_here > target:
            return 0

        if sum_here == target:
            return 1

        return sum([recurse(sum_here + num) for num in nums])

    return recurse(0)

def recursive_memoize(nums, target):
    cache = {}
    def recurse(sum_here):
        if sum_here in cache:
            return cache[sum_here]

        if sum_here > target:
            cache[sum_here] = 0

        elif sum_here == target:
            cache[sum_here] = 1

        else:
            cache[sum_here] = sum([recurse(sum_here + num) for num in nums])

        return cache[sum_here]

    return recurse(0)

"""
4
1, 2, 3

[0, 0, 0, 0, 1]
[0, 1, 1, 1, 1]
[1, 2, 2, 1, 1]
[3, 4, 2, 1, 1]
[7, 4, 2, 1, 1]
"""

def tableu(nums, target):
    cache = [0 for _ in range(target + 1)]
    cache[-1] = 1
    for i in range(target, -1, -1):
        if cache[i] == 0:
            continue
        for num in nums:
            if i - num >= 0:
                cache[i-num] += cache[i]
    return cache[0]


nums = [1, 2, 3]
target = 4

# nums = [4, 2, 1]
# target = 32

print recursive_memoize(nums, target)
print tableu(nums, target)