
def counting_sort(arr):
    # assume all ints between 0 - 10 for counts
    counts = [0] * 10
    output = [0] * len(arr)

    for el in arr:
        counts[el] += 1

    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i-1]

    for el in arr:
        index = counts[el] - 1
        output[index] = el
        counts[el] -= 1

    return output


if __name__ == '__main__':
    arr = [6, 7, 5, 6, 6, 5, 3, 1, 3, 2, 4, 5, 8, 4]
    print counting_sort(arr)