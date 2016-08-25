"""
CodeAbbey, Problem 138
Coded by whoisrgj
"""
from collections import Counter


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        if self.value:
            return "%r" % self.value
        else:
            return "({},{})".format(self.left, self.right)


class HuffmanCoding(object):
    def __init__(self, string):
        self.string = string
        self.counter = Counter(string)
        self.root = self._build_tree()
        self.bit_sequence = dict()
        self._generate_bit_sequence(self.root, "")

    def _build_tree(self):
        letter_count = list(self.counter.items())
        nodes = [(count, Node(value=letter)) for letter, count in letter_count]
        nodes.sort(key=lambda x: (x[1].value, -x[0]))
        while len(nodes) >= 2:
            right, left = nodes.pop(), nodes.pop()
            node = Node(left=left[1], right=right[1])
            nodes.append((left[0]+right[0], node))
            nodes.sort(key=lambda x: x[0], reverse=True)
        return nodes.pop()[1]

    def _generate_bit_sequence(self, node, bit_sequence):
        if node.value:
            self.bit_sequence[node.value] = bit_sequence
        else:
            self._generate_bit_sequence(node.left, bit_sequence + "1")
            self._generate_bit_sequence(node.right, bit_sequence + "0")

    @property
    def ratio(self):
        original_size = len(self.string) * 8
        compressed_size = sum(self.counter[c] * len(self.bit_sequence[c])
                              for c in self.bit_sequence.keys())
        return original_size / compressed_size


def main():
    hc = HuffmanCoding(input())
    print(hc.ratio)


if __name__ == '__main__':
    main()
