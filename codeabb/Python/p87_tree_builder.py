"""
CodeAbbey, Problem 87
Coded by whoisrgj
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def print_node(self, node):
        if node:
            return "({},{},{})".format(self.print_node(node.left), node.value, self.print_node(node.right))
        else:
            return "-"

    def __str__(self):
        return self.print_node(self.root)


def main():
    n = int(input())  # not used
    values = list(map(int, input().split()))
    tree = Tree()
    for value in values:
        tree.add(value)
    print(tree)

if __name__ == '__main__':
    main()
