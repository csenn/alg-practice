def lcm(a, b):
    my_dict = {}
    for i in range(1, b):
        my_dict[ a*i ] = True

    for i in range(1, a):
        if my_dict[ b*i ]:
            return b*i

    return a * b

print 10, lcm(2, 10)
print 10, lcm(3, 10)
