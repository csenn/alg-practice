# https://leetcode.com/problems/container-with-most-water

# naieve 1
# def get_area(arr, i, j):
#     heights = sorted([arr[i], arr[j]])
#     return (j - i) * min(heights[1], heights[0])

# def calc(arr):
#     arr_len = len(arr)
#     max_area = 0
#     for i in range(arr_len):
#         for j in range(i+1, arr_len):
#             max_area = max(max_area, get_area(arr, i, j))
#     return max_area


# naieve 1
# def get_area(i, j, h1, h2):
#     return abs(i - j) * min(h1, h2)

# def calc(arr):
#     tup_arr = []
#     for i, num in enumerate(arr):
#         tup_arr.append((num, i))

#     tup_arr.sort(key=lambda node: node[0], reverse=True)
#     tup_arr_len = len(tup_arr)
#     max_area = 0
#     i = 0
#     counter = 0
#     while i < tup_arr_len:
#         curr_height, curr_i = tup_arr[i]
#         right = tup_arr_len - 1
#         left = 0

#         l_done = False
#         r_done = False
#         while True:
#             l_finish = l_done or left >= curr_i
#             r_finish = r_done or right <= curr_i

#             if l_finish and r_finish:
#                 break

#             if not l_finish:
#                 max_left = (curr_i - left) * curr_height
#                 if max_left < max_area:
#                     l_done = True
#                 else:
#                     area_left = get_area(curr_i, left, curr_height, arr[left])
#                     max_area = max(max_area, area_left)
#                     left += 1
#             if not r_finish:
#                 max_right = (right - curr_i) * curr_height
#                 if max_right < max_area:
#                     r_done = True
#                 else:
#                     area_right = get_area(curr_i, right, curr_height, arr[right])
#                     max_area = max(max_area, area_right)
#                     right -= 1
#         i += 1
#     return max_area

# FUCK
def calc(arr):
    left = 0
    right = len(arr) - 1
    mx = 0
    while left < right:
        mx = max(mx, (right - left) * min(arr[left], arr[right]))
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return mx

# print calc([1,1])
print calc([1, 6, 2, 7, 3, 2, 9, 1])