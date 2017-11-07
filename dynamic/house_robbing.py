def rob(nums):
    nums_len = len(nums)
    def recurse(index):
        if index >= nums_len:
            return 0

        return max(
            nums[index] + recurse(index + 2),
            recurse(index + 1)
        )
    return recurse(0)

def rob_memoize(nums):
    nums_len = len(nums)
    cache = {}

    def recurse(index):
        if index not in cache:
            if index >= nums_len:
                cache[index] = 0
            else:
                cache[index] = max(
                    nums[index] + recurse(index + 2),
                    recurse(index + 1)
                )
        return cache[index]
    return recurse(0)

""" 
 1 2 3 4 5
         5

2, 1, 1, 2

         2

"""
def rob_dynamic(nums):
    if len(nums) < 3:
        return max(nums)

    num_len = len(nums)

    for i in range(num_len-1, -1, -1):
        two = nums[i+2] if i+2 < num_len else 0
        one = nums[i+1] if i+1 < num_len else 0
        nums[i] = max(
            nums[i] + two,
            one
        )
    return nums[0]



nums = [1, 2, 3, 4, 5]
nums = [2, 1, 1, 2]

print rob(nums)
print rob_memoize(nums)
print rob_dynamic(nums)