"""
CodeAbbey, Problem 136
Coded by Raul Gonzalez
"""


class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self):
        self.root = Node()

    def get_root(self):
        return self.root

    def add(self, value, string):
        p = self.root
        for c in list(string):
            if c == '0':
                if p.left is None:
                    p.left = Node()
                p = p.left
            else:
                if p.right is None:
                    p.right = Node()
                p = p.right
        p.value = value


class Problem136:
    def __init__(self, string):
        self.encoded_str = string
        self.encoding_map = {
            ' ': "11",
            'a': "011",
            'b': "0000010",
            'c': "000101",
            'd': "00101",
            'e': "101",
            'f': "000100",
            'g': "0000100",
            'h': "0011",
            'i': "01001",
            'j': "000000001",
            'k': "0000000001",
            'l': "001001",
            'm': "000011",
            'n': "10000",
            'o': "10001",
            'p': "0000101",
            'q': "000000000001",
            'r': "01000",
            's': "0101",
            't': "1001",
            'u': "00011",
            'v': "00000001",
            'w': "0000011",
            'x': "00000000001",
            'y': "0000001",
            'z': "000000000000",
            '!': "001000"
        }
        self.tree = self.populate_tree()
        self.decoding_map = self.create_decode_map()

    def populate_tree(self):
        t = Tree()
        for k in self.encoding_map.keys():
            t.add(k, self.encoding_map[k])
        return t

    @staticmethod
    def create_decode_map():
        decode_map = dict()
        for x in range(10):
            decode_map[str(x)] = x
        for x in range(10, 32):
            decode_map[chr(55 + x)] = x
        return decode_map

    def solve(self):
        binary_str = ""
        for x in range(len(self.encoded_str)):
            binary_str += '{0:05b}'.format(self.decoding_map[self.encoded_str[x]])

        p = self.tree.get_root()
        for c in list(binary_str):
            if c == '0':
                p = p.left
            else:
                p = p.right
            if p.value is not None:
                print(p.value, end="")
                p = self.tree.get_root()
        # end solve
# end class


if __name__ == "__main__":
    Problem136(input()).solve()
