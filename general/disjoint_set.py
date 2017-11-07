import time
start_time = time.time()

class Disjoint_Set:
    def __init__(self, n):
        self.nodes = {}
        for index in range(1, n + 1):
            i = str(index)
            self.nodes[i] = { 'val': i, 'parent': i, 'rank': 0, 'size': 1 }

    def union(self, a, b):
        a_root = self.find_root(a)
        b_root = self.find_root(b)
        if a_root == b_root:
            return
        if a_root['rank'] > b_root['rank']:
            b_root['parent'] = a_root['val']
            a_root['size'] += b_root['size']
        elif a_root['rank'] < b_root['rank']:
            a_root['parent'] = b_root['val']
            b_root['size'] += a_root['size']
        else:
            b_root['parent'] = a_root['val']
            a_root['size'] += b_root['size']
            a_root['rank'] += 1

    def find_root(self, a):
        node = self.nodes[a]
        updates = []
        while node['val'] != node['parent']:
            updates.append(node)
            node = self.nodes[node['parent']]
        # update node as a caching optimization
        for update in updates:
            update['parent'] = node['val']
        return node
    def find_size(self, a):
        return self.find_root(a)['size']

if __name__ == '__main__':
    f = open('temp_data.txt', 'r') #268
    # f2 = open('temp_data_2.txt', 'r')
    n, q = [int(i) for i in f.readline().strip().split()]
    ds = Disjoint_Set(n)
    for _ in range(int(q)):
        arr = f.readline().strip().split()
        if arr[0] == 'M':
            ds.union(arr[1], arr[2])
        else:
            pass

    print("--- %s seconds ---" % (time.time() - start_time))
            # print ds.find_size(arr[1])
            # val2 = f2.readline().strip()
            # if val2 != str(val):
                # print count, 'wrong', val2, val
