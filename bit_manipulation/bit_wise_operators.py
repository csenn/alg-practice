# shift bits over by y
num = 3
for i in range(25):
    shifted = i << num
    print i, shifted, format(i, 'b'), format(shifted, 'b')

print '\n--------\n'

nums = [
    [1, 1],
    [1, 2],
    [2, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [1, 6],
    [1, 7],
]

for num in nums:
    print num[0], num[1], num[0] & num[1], format(num[0], 'b'), format(num[1], 'b'), format(num[0] & num[1], 'b')