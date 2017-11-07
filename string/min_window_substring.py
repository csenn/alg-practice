"""
    When trying to find if a substring matches some requirements
    in a string, a sliding window approach works.

    You iterate as far out with an end pointer until some requiremnt is met.

    The you iterate your start string as long as the condition is still met.

    Once that fails, you continue on iterating end.
"""
from collections import defaultdict

def calc(string, search):

    curr_map = defaultdict(int)
    search_map = {}

    for letter in search:
        if letter not in search_map:
            search_map[letter] = 0
        search_map[letter] += 1

    start, end, needed = 0, 0, len(search)

    min_len = 2147483647
    min_str = ''

    str_len = len(string)
    while end < str_len:
        end_letter = string[end]
        curr_map[end_letter] += 1

        # if our added letter is less then or equal to what we are searching for
        # we know this addition should reduce what we needed
        if end_letter in search_map and curr_map[end_letter] <= search_map[end_letter]:
            needed -= 1

        while needed == 0:
            if end - start < min_len:
                min_len = end - start
                min_str = string[start: end + 1]

            start_letter = string[start]
            curr_map[start_letter] -= 1

            if start_letter in search_map and curr_map[start_letter] < search_map[start_letter]:
                needed += 1
            start += 1

        end += 1
    return min_str


if __name__ == '__main__':
    print calc('ADOBECODEBANC', 'ABC')
    # print calc('AAAABAAACCCACB', 'ABC')