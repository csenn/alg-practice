def subsets(init_arr):
    arr_len  = len(init_arr)
    results = [init_arr]

    def recurse(index, arr):
        for i in range(index, arr_len):
            next_arr = list(arr)
            next_arr.append(init_arr[i])
            results.append(next_arr)
            recurse(i + 1, next_arr)

    recurse(0, [])
    print results
    print len(results), 'should be', pow(2, arr_len)

arr = [7, 8, 9, 10]
print subsets(arr)