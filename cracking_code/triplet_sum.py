"""
Given an array S of n integers, are there
elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.


"""

from collections import defaultdict

# naieve approach worked, just too slow
# def calc(nums):
#     # set_len = len(my_set)
#     arr = nums
#     arr_len = len(arr)
#     my_dict = defaultdict(list)
#     for i in range(arr_len):
#         if i+1 is not arr_len and arr[i] == arr[i+1]:
#             continue

#         for j in range(i + 1, arr_len):
#             if j+1 is not arr_len and arr[j] == arr[j+1]:
#                 continue

#             sum_val = arr[i] + arr[j]
#             my_dict[sum_val].append((i, j))

#     final = {}
#     for i in range(arr_len):
#         need = 0 - arr[i]
#         for index_x, index_y in my_dict[need]:
#             if index_x == i or index_y == i:
#                 continue
#             key = tuple(sorted( [ arr[i], arr[index_x], arr[index_y] ] ))
#             final[key] = True

#     return final.keys()


def calc(nums):
    nums.sort()
    num_len = len(nums)
    i = 0

    final = {}
    while i < num_len - 2:
        if i>1 and nums[i-2] == nums[i]:
            i += 1
            continue
        l = i + 1
        r = num_len - 1
        while l < r:
            val = nums[i] + nums[l] + nums[r]
            if val < 0:
                l += 1
            elif val > 0:
                r -= 1
            else:
                key = tuple(sorted([nums[i], nums[l], nums[r]]))
                final[key] = True
                l += 1
                r -= 1
        i += 1

    return final.keys()

# print calc([-1, 0, 1, 2, -1, -4])
# print calc([1, -1, -1, 0])
print calc([3,0,-2,-1,1,2])