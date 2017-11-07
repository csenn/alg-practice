"""

"""

tracker = {
    'a': 0,
    'b': 0
}

# recursive
def calc(n):
    tracker['a'] += 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return calc(n-1) + calc(n-2)


# dynamic memoize
def calc_memoize(n):
    vals = {1:1, 2:2}
    def recurse(n):
        tracker['b'] += 1
        if n not in vals:
            vals[n] = recurse(n-1) + recurse(n-2)
        return vals[n]
    return recurse(n)

# dynamic
def calc_tableu(n):
    # vals = [-1] * (n + 1)
    val_1 = 1
    val_2 = 2
    if n == 1:
        return val_1
    if n == 2:
        return val_2

    for i in range(2, n):
        temp = val_1 + val_2
        val_1 = val_2
        val_2 = temp

    return val_2

for i in range(1, 15):
    print calc(i), calc_memoize(i), calc_tableu(i)

print tracker
# print 1, calc(1)
# print 2, calc(2)
# print 3, calc(3)
# print calc(4)
