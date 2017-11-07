
class Heap:
    def __init__(self):
        self._heap = []

    def swap(self, i, j):
        temp = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = temp

    def add(self, val):
        self._heap.append(val)
        self.perc_up(len(self._heap) - 1)

    def remove(self, val):
        index = self._heap.index(val)
        self.swap(index, len(self._heap) - 1)
        self._heap.pop()
        self.perc_down(index)

    def perc_up(self, index):
        parent_index = index / 2
        if self._heap[parent_index] > self._heap[index]:
            self.swap(index, parent_index)
            self.perc_up(parent_index)

    def perc_down(self, index):
        heap_len = len(self._heap)
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < heap_len and self._heap[left] < self._heap[smallest]:
            smallest = left

        if right < heap_len and self._heap[right] < self._heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(smallest, index)
            self.perc_down(smallest)

if __name__ == '__main__':
    heap = Heap()
    els = [6, 7, 2, 3, 6, 1, 8, 12, 5, 3, 23]
    for el in els:
        heap.add(el)