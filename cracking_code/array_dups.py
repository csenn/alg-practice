import bisect





def containsNearbyAlmostDuplicate(nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """

    if len(nums) < 2:
        return False
    start = 0
    num_len = len(nums)
    init_options = nums[1:k + 1] if k + 1 < num_len else nums[1:num_len]
    init_options.sort()

    while start < num_len and len(init_options) > 0:
        possible_index = bisect.bisect_left(init_options, nums[start])
        indexes = [possible_index - 1, possible_index, possible_index + 1]
        for index in indexes:
            if  index < len(init_options) and abs(nums[start] - init_options[index]) <= t:
                return True

        # print possible_index,  init_options



        # if possible_index + 1 < len(init_options) and abs(nums[start] - init_options[possible_index + 1]) <= t:
        #     return True

        # or abs(nums[start] - init_options[-1]) <= t:
        #     return True

        start += 1
        del init_options[bisect.bisect_left(init_options, nums[start])]
        if start + k < num_len:
            bisect.insort(init_options, nums[start + k])

    return False


# containsNearbyAlmostDuplicate([-1, -1], 1, -1)
print containsNearbyAlmostDuplicate(
    [4, 1, 6, 3],
    100,
    1
)