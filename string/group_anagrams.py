def transform(string):
    arr = [0] * 26
    for letter in string:
        arr[ord(letter)-97] += 1
    return tuple(arr)

def groupAnagrams(strs):
    my_dict = {}
    for string in strs:
        tup = transform(string)
        if tup not in my_dict:
            my_dict[tup] = []
        my_dict[tup].append(string)

    return my_dict.values()

print groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])