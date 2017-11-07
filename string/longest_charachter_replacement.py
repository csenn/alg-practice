from collections import defaultdict

def decide(my_dict, k):
    vals = my_dict.values()
    max_val = max(vals)
    key_sum = sum(vals)
    rest = key_sum - max_val
    if rest > k:
        return False, key_sum
    return True, key_sum


def calc(s, k):
    s_len = len(s)
    max_counter = 0
    l, r = 0, 0
    my_dict = defaultdict(int)
    result = 0
    my_dict[s[0]] = 1

    while True:
        move_right, count = decide(my_dict, k)
        # print move_right, count
        if move_right:
            r += 1
            result = max(result, count)
            if r == s_len:
                break
            my_dict[s[r]] += 1
        else:
            l += 1
            if l == s_len:
                break
            my_dict[s[l-1]] -= 1

    return result

print calc('ABAB', 2)
print calc('AABABBA', 1)
print calc("BAAAB", 2)
print 2, calc("ABAA", 0)
