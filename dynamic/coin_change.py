"""
Try each and every coin
Then try each and every coin

[10, 8, 1] 116

10 * 9 + 8 * 2 = 11
10 * 10 + 6 * 1 = 16
"""
import sys
sys.setrecursionlimit(10**6)

tracker = {
    'a': 0,
    'b': 0,
    'c': 0
}

# naieve recursion
def recursive(init_target, vals):
    max_int = 9223372036854775807

    def calc(target, iterator):
        if target < 0:
            return max_int
        if target == 0:
            return iterator

        tracker['a'] += 1

        return min(map(lambda x: calc(target - x, iterator + 1), vals))

    val = calc(init_target, 0)
    return -1 if val == max_int else val


def dynamic_memoize(amount, coins):

    # Sort reverse to start with larger coins first
    coins.sort(reverse = True)
    max_int = 9223372036854775807
    cache = {}

    # Exit if too deep
    best_min = {'val': max_int}

    def calc(target, iterator):
        if iterator > best_min['val'] or target < 0:
            return max_int

        # if target % coins[0] == 0:
        #     iterator += target / coins[0]
        #     target = 0
        #     print 'hah', iterator

        if target == 0:
            if iterator < best_min['val']:
                best_min['val'] = iterator
            return iterator

        tracker['b'] += 1

        if (target, iterator) not in cache:
            cache[(target, iterator)] = min(map(lambda x: calc(target - x, iterator + 1), coins))

        return cache[(target, iterator)]

    val = calc(amount, 0)
    return -1 if val == max_int else val


# def get_min_col(matrix, a, c_len):
#     min_val = None
#     for i in range(c_len):
#         val = matrix[i][a]
#         if val is not None and (min_val == None or val < min_val) :
#             min_val = val
#     return min_val


# def coinChange(self, coins, amount):
#     c_len = len(coins)
#     matrix = [[None for _ in range(amount + 1)] for _ in range(c_len)]
#     prev_min = {}

#     for a in range(amount + 1):
#         for c in range(c_len):
#             coin = coins[c]
#             if a == 0:
#                 matrix[c][a] = 0
#             elif a - coin >= 0:
#                 if a - coin not in prev_min:
#                     prev_min[a-coin] = get_min_col(matrix, a - coin, c_len)
#                 # min_val = get_min_col(matrix, a - coin, c_len)
#                 matrix[c][a] = prev_min[a-coin] + 1 if prev_min[a-coin] != None else None
#     result = get_min_col(matrix, amount, c_len)
#     return -1 if result == None else result

def dynamic_tableu(amount, coins):
    c_len = len(coins)
    mins = [-1 for _ in range(amount + 1)]
    mins[0] = 0

    for a in range(1, amount + 1):
        for c in range(c_len):
            tracker['c'] += 1
            coin = coins[c]
            if a - coin >= 0:
                min_val = mins[a-coin]
                if min_val == -1:
                    continue
                if mins[a] == -1 or min_val + 1 < mins[a]:
                    mins[a] = min_val + 1
    return mins[amount]


# print recursive(11, [1, 2, 5])
# print dynamic_memoize(11, [1, 2, 5])
# print dynamic_memoize(8839, [3,7,405,436])
# print dynamic_tableu(8839, [3,7,405,436])
# print dynamic_tableu(1, [2])
# print dynamic_memoize(1541, [48,477,450,440,59,295,429])
# print dynamic_tableu(1541, [48,477,450,440,59,295,429])

print dynamic_memoize(8402, [125,146,125,252,226,25,24,308,50])
print dynamic_tableu(8402, [125,146,125,252,226,25,24,308,50])

# print dynamic_tableu(10, [1, 3, 7])
print tracker