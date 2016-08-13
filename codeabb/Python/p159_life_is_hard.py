"""
CodeAbbey, Problem 159
Coded by whoisrgj
"""


class LifeIsHard(object):

    GENERATIONS_TO_STABILIZE = 5

    def __init__(self):
        self.organisms = set()

    def start(self):
        self.get_organisms_from_input()
        stable = last_result = generation = 0
        while stable < self.GENERATIONS_TO_STABILIZE:
            self.process_turn()
            generation += 1
            if last_result == len(self.organisms):
                stable += 1
            else:
                stable = 0
            last_result = len(self.organisms)
        print(generation-self.GENERATIONS_TO_STABILIZE, len(self.organisms))

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

    def get_organisms_from_input(self):
        ref_x, ref_y = map(int, input().split())
        self.organisms.update(self.get_glider_coordinates())
        self.organisms.update(self.get_acorn_coordinates(ref_x, ref_y))

    @staticmethod
    def get_neighbors(row, col):
        t = (-1, 0, 1)
        return [(row+i, col+j) for i in t for j in t if not (i == j == 0)]

    @staticmethod
    def get_acorn_coordinates(ref_x, ref_y):
        t = ((0, 0), (0, 1), (-1, 0), (-1, 2), (-2, 0))
        return [(ref_x+i, ref_y+j) for i, j in t]

    @staticmethod
    def get_glider_coordinates():
        return [(0, 0), (1, 0), (1, 2), (3, 1), (4, 0), (5, 0), (6, 0)]


def main():
    lih = LifeIsHard()
    lih.start()

if __name__ == '__main__':
    main()
