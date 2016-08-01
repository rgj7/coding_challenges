"""
CodeAbbey, Problem 72
Coded by whoisrgj
"""


class LifeIsSimple(object):

    COLUMNS = 7
    ROWS = 5
    TURNS = 5

    def __init__(self):
        self.organisms = set()

    def start(self):
        self.get_organisms_from_input()
        results = []
        for _ in range(self.TURNS):
            self.process_turn()
            results.append(len(self.organisms))
        print(*results)

    def process_turn(self):
        marked_to_die = []
        marked_for_birth = []
        empty_neighbors = set()
        # mark organisms to die
        for row, col in self.organisms:
            alive_neighbors = 0
            for neighbor in self.get_neighbors(row, col):
                if neighbor in self.organisms:
                    alive_neighbors += 1
                else:
                    empty_neighbors.add(neighbor)
            if not 2 <= alive_neighbors <= 3:
                marked_to_die.append((row, col))
        # mark organisms for birth
        for row, col in empty_neighbors:
            alive_neighbors = 0
            for neighbor in self.get_neighbors(row, col):
                if neighbor in self.organisms:
                    alive_neighbors += 1
            if alive_neighbors == 3:
                marked_for_birth.append((row, col))
        # remove/add marked organisms
        for organism in marked_to_die:
            self.organisms.remove(organism)
        for organism in marked_for_birth:
            self.organisms.add(organism)

    @staticmethod
    def get_neighbors(row, col):
        t = (-1, 0, 1)
        return [(row+i, col+j) for i in t for j in t if not (i == j == 0)]

    def get_organisms_from_input(self):
        for i in range(self.ROWS):
            row = input()
            for j, c in enumerate(row):
                if c == 'X':
                    self.organisms.add((i, j))


def main():
    ls = LifeIsSimple()
    ls.start()

if __name__ == '__main__':
    main()
