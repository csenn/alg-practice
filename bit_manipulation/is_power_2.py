def is_power_2(num):
    string = format(num, 'b')
    if len(string) < 2 or string[0] != '1':
        return False

    for i in range(1, len(string)):
        if string[i] != '0':
            return False

    return True


print False, is_power_2(1)
print True, is_power_2(2)
print False, is_power_2(3)
print True, is_power_2(4)
print False, is_power_2(5)
print False, is_power_2(6)
print True, is_power_2(8)
print True, is_power_2(16)
print False, is_power_2(17)
print True, is_power_2(64)