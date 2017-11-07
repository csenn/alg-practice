import time
"""
ABCD
D

C
CD

B
BD
BC
BCD
"""

counter = {
    'a': 0,
    'b': 0,
    'c': 0
}

# Each dict will have 2^n keys where n is length of string
def get_dict(a):
    a_len = len(a)
    vals = { a[a_len-1]: 1 }
    for i in range(a_len-2, -1, -1):
        curr = a[i]
        words = vals.keys()
        for word in words:
            next_word = curr + '_' + word
            vals[next_word] = len(next_word)
        vals[curr] = 1
    return vals

# print len(get_dict('a'))
# print len(get_dict('ab'))
# print len(get_dict('abc'))
# print len(get_dict('abcd'))
# print len(get_dict('abcde'))
# print len(get_dict('abcdef'))
# print len(get_dict('abcdefg'))

def lcs_naive(a, b):
    a_dict = get_dict(a)
    b_dict = get_dict(b)

    max_val = 0
    max_key = ''
    a_keys = a_dict.keys()

    for a_key in a_keys:
        if a_key in b_dict:
            key_len = len(a_key)
            if key_len > max_val:
                max_key = a_key
                max_val = key_len
    return max_key.replace('_', ' ')

"""
ADH ABCDGH
Figure out if a subpattern exits in a bigger pattern
"""
def lcs_subpattern(a, search):
    i, j = 0, 0
    i_len, search_len = len(a), len(search)
    while i < i_len and j < search_len:
        if a[i] == search[j]:
            j += 1
            if j == search_len:
                return True
        i += 1
    return False

# still need to find every subpattern for one string
def combine_naive_and_warmup(a, b):
    a_dict = get_dict(a)
    searches = a_dict.items()
    searches.sort(key=lambda x: x[1], reverse=True)
    for search in searches:
        search_arr = search[0].split('_')
        if lcs_subpattern(b, search_arr):
            return ' '.join(search_arr)
    return -1
"""
A B C D G H

A E D F H R

We start with our main string (which is smaller)
and we figure out how
many matches there are in index - 1 matches

Here we are finding every subpattern for the 

"""
def lcs_optimized(a, b):
    main, search = (a, b) if len(a) < len(b) else (b, a)
    main_len = len(main)
    arr = [main[-1]]

    for i in range(main_len - 2, -1, -1):
        curr = main[i]
        for j in range(len(arr)):
            next_word =  curr + ' ' + arr[j]
            pattern = next_word.split(' ')
            # only add larger patterns if sub patterns match
            if lcs_subpattern(search, pattern):
                arr.append(next_word)
        arr.append(curr)

    return max(arr, key=len)


"""
n e m a t o d e
  e m p t

There are 3 possibilites.
  - The first charachters of the strings match
  - They dont and we progress one string by an index
  - They dont and we progress the other string by an index
"""

def lcs_recursive(a, b):
    a_len = len(a)
    b_len = len(b)

    def recurse(i, j, match_str):
        if i == a_len or j == b_len:
            return match_str

        if a[i] == b[j]:
            return recurse(i + 1, j + 1, match_str + ' ' + a[i])

        return max(
            recurse(i + 1, j, match_str),
            recurse(i, j + 1, match_str),
            key=len
        )

    return recurse(0, 0, '').strip()


def lcs_recursive_memoize(a, b):

    a_len = len(a)
    b_len = len(b)
    cache = {}

    def recurse(i, j, match_str):
        if (i, j, match_str) in cache:
            return cache[(i, j, match_str)]

        if i == a_len or j == b_len:
            val = match_str
        elif a[i] == b[j]:
            val = recurse(i + 1, j + 1, match_str + ' ' + a[i])
        else:
            val = max(
                recurse(i + 1, j, match_str),
                recurse(i, j + 1, match_str),
                key=len
            )

        cache[(i, j, match_str)] = val
        return val

    return recurse(0, 0, '').strip()

"""
  N E M A T O
E 0 1 1 1 1 1
M 0 1 2 2 2 2
P 0 1 2 2 2 2
T 0 1 2 2 3 3
Y 0 1 2 2 3 3
R 0 1 2 2 3 3

  A B C D
B 0 1 1 1
C 0 1 2 2
E 0 1 2 2
C 0 1 2 3

"""

def lcs_tableu(a, b):
    a_len, b_len = len(a), len(b)
    matrix = [[0 for _ in range(b_len + 1)] for _ in range(a_len + 1)]

    i, j = 0, 0

    # while i < a_len and b < b_len:
    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            if a[i-1] == b[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    vals = []
    i, j = a_len, b_len
    while i > 0 and j > 0:
        if matrix[i-1][j] == matrix[i][j]:
            i -= 1
        elif matrix[i][j-1] == matrix[i][j]:
            j -= 1
        else:
            vals.append(a[i-1])
            i -= 1
            j -= 1

    vals.reverse()

    return ' '.join(vals)


arr_a = list('ABCDGH')
arr_b = list('AEDFHR')

# arr_c = '16 27 89 79 60 76 24 88 55 94 57 42 56 74 24 69 29 14 7 94 41 3 23 49 84 78 73 63 5 4'.split()
# arr_d = '27 16 88 0 55 89 94 79 34 42 76 47 88 74 57 46 24 5 43 89 43 3 23 35 84 98 47 89 73 24 20 14'.split()

arr_c = '16 27 89 79 60 76 24 88 55 94 57 42 56 74 24 95 55 33 69 29 14 7 94 41 8 71 12 15 43 3 23 49 84 78 73'.split()
arr_d = '27 76 88 0 55 99 94 70 34 42 31 47 56 74 69 46 93 88 89 7 94 41 68 37 8 71 57 15 43 89 43'.split()

arr_e = list('NEMATO')
arr_f = list('EMPYTR')

arr_g = '1 2 3 4 1'.split()
arr_h = '3 4 1 2 1 3'.split()

# arr_c = '16 27 89 79 60 76 24 88 55 94 57 42 56 74 24 95 55 33 69 29 14 7 94 41 8 71 12 15 43 3 23 49 84 78 73 63 5 46 98 26 40 76 41 89 24 20 68 14 88 26'.split()
# arr_d = '27 76 88 0 55 99 94 70 34 42 31 47 56 74 69 46 93 88 89 7 94 41 68 37 8 71 57 15 43 89 43 3 23 35 49 38 84 98 47 89 73 24 20 14 88 75'.split()

# result_c = [1, 3, 5, 6, 7, 8, 9, 10]
# result_d = [0, 1, 3,  6, 7, 8, 9, 10]

# print get_dict(arr_a)


# def assert_true(result, expected):
    # assert len(result) == len(expected)
    # for i, val in enumerate(result):
        # assert val == expected[i]

# assert_true(lcs_naive(arr_a, arr_b),'A D H')

# assert 'A D H' == lcs_naive(arr_a, arr_b)
# assert 'A D H' == combine_naive_and_warmup(arr_a, arr_b)
# assert 'A D H' == lcs_recursive(arr_a, arr_b)

# start_time = time.time()
# print lcs_naive(arr_c, arr_d)
# b = time.time()
# print start_time - b
# b = time.time




# c = time.time()
# print lcs_optimized(arr_c, arr_d)
# d = time.time()
# print d - c

print lcs_recursive_memoize(arr_c, arr_d)
# print  time.time() - d

print lcs_tableu(arr_c, arr_d)
print lcs_tableu(arr_g, arr_h)






# print lcs_tableu(arr_e, arr_f)

# print arr_c

# print 'ADH', lcs_naive(str_a, str_b)

# assert_true(lcs_subpattern('ABCDGH', 'ADH'), ['A', 'D', 'H'])

# print True, lcs_subpattern('ABCDGH', 'ADH')
# print False, lcs_subpattern('ABCDGH', 'ADOH')

# print 'GTAB', lcs_naive('AGGTAB', 'GXTXAYB')

# print 'ADH', combine_naive_and_warmup(str_a, str_b)
# print 'GTAB', combine_naive_and_warmup('AGGTAB', 'GXTXAYB')

# print 'GTAB', lcs_recursive('AGGTAB', 'GXTXAYB')

# print 'ADH', combine_naive_and_warmup(str_a, str_b)

# print lcs_recursive(arr_a, arr_b)
# assert 'A D H' == lcs_recursive(arr_a, arr_b)
# print lcs_recursive_memoize(arr_c, arr_d)
# assert 'A D H' == lcs_recursive_memoize(arr_a, arr_b)


