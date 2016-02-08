"""
CodeAbbey, Problem 92
Coded by whoisrgj
"""

import math


class BinaryHeap:
    def __init__(self):
        self.values = list()

    def put(self, value):
        self.values.append(value)
        index = len(self.values)-1
        while index != 0:
            parent_index = self.get_parent_index(index)
            if self.values[parent_index] > self.values[index]:
                self.swap(parent_index, index)
                index = parent_index
            else:
                break

    def extract_min(self):
        root_value = self.values[0]
        self.values[0] = self.values.pop()
        ptr = current = 0
        while self.cell_exist(current):
            left, right = self.get_children_indices(current)
            if self.cell_exist(left) and self.cell_exist(right):
                ptr = self.get_min_index(left, right)
            elif self.cell_exist(left) and self.values[left] < self.values[ptr]:
                ptr = left
            elif self.cell_exist(right) and self.values[right] < self.values[ptr]:
                ptr = right
            if ptr != current:
                self.swap(ptr, current)
                current = ptr
            else:
                break
        return root_value

    def swap(self, idx1, idx2):
        self.values[idx1], self.values[idx2] = self.values[idx2], self.values[idx1]

    def get_min_index(self, idx1, idx2):
        return idx1 if self.values[idx1] < self.values[idx2] else idx2

    def cell_exist(self, idx):
        return idx < len(self.values)

    @staticmethod
    def get_parent_index(k):
        return int(math.floor((k-1)/2))

    @staticmethod
    def get_children_indices(k):
        return 2*k+1, 2*k+2

    def __str__(self):
        return " ".join(map(str, self.values))


if __name__ == '__main__':
    N = int(input())
    array_values = list(map(int, input().split()))
    heap = BinaryHeap()
    for v in array_values:
        if v != 0:
            heap.put(v)
        else:
            heap.extract_min()
    print(heap)
