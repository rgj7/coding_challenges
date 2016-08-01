"""
CodeAbbey, Problem 72
Coded by whoisrgj
"""


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
    n, initial_seed = map(int, input().split())
    word_lengths = list(map(int, input().split()))
    fwg = FunnyWordGenerator(initial_seed)
    print(" ".join(fwg.generate(l) for l in word_lengths))


if __name__ == "__main__":
    main()

