"""
0 000
1 001

2 010
3 011

4 100
5 101
6 110
7 111
"""

# http://interactivepython.org/runestone/static/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html

digits = "0123456789ABCDEF"

def divideBy2(decNumber, base):
    remstack = []

    while decNumber > 0:
        rem = decNumber % base
        remstack.append(rem)
        decNumber = decNumber // base

    binString = ""
    while not len(remstack) == 0:
        binString += digits[remstack.pop()]
    return binString

def p_num(num):
    anwer = divideBy2(num, 2)
    print num, anwer

p_num((0))
p_num((1))
p_num((2))
p_num((3))
p_num((4))
p_num((5))
p_num((6))
p_num((7))
p_num((8))
p_num((12))
p_num((123))
p_num((321))
p_num((1230))
p_num((12300))
p_num((123000))
p_num((1230000))
p_num((12300000))
p_num((123000000))
p_num((1230000000))
p_num((12300000000))
p_num((123000000000))
p_num((1230000000000))
p_num((12300000000000))
p_num((123000000000000))
p_num((1230000000000000))
p_num((12300000000000000))
p_num((123000000000000000))
p_num((1230000000000000000))
     # 9223372036854775807 maxInt
p_num((12300000000000000000)) # 20 digits, 64 bits
p_num((123000000000000000000))

# 12,300,000,000,000,000,000


