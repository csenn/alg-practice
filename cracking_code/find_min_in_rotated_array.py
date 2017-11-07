"""
  Use a binary search like approach
  4 5 6 7 0 1 2
"""

def get_min(nums, low, high):
    if high - low == 0:
        return nums[high]
    midpoint = low + (high-low) / 2
    if nums[midpoint] > nums[high]:
        return get_min(nums, midpoint + 1, high)
    return get_min(nums, low, midpoint)

def findMin(nums):
    return get_min(nums, 0, len(nums) - 1)

print findMin([4, 5, 6, 7, 0, 1, 2])