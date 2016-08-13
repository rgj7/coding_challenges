"""
CodeAbbey, Problem 70
Coded by whoisrgj
"""
from collections import Counter

WORD_LIMIT = 900000
WORD_LENGTH = 6


class FunnyWordGenerator(object):
    CONSONANTS = "bcdfghjklmnprstvwxz"
    VOWELS = "aeiou"

    def __init__(self, initial_seed):
        self.seed = initial_seed

    def generate(self, word_length):
        word = []
        for i in range(word_length):
            self.seed = (445 * self.seed + 700001) % 2097152
            letters = self.VOWELS if i % 2 else self.CONSONANTS
            word.append(letters[self.seed % len(letters)])
        return "".join(word)


def main():
    seed = int(input())
    fwg = FunnyWordGenerator(seed)
    counter = Counter()
    for _ in range(WORD_LIMIT):
        word = fwg.generate(WORD_LENGTH)
        counter[word] += 1
    print(counter.most_common(1)[0][0])

if __name__ == '__main__':
    main()
