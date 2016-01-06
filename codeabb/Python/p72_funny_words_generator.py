"""
CodeAbbey, Problem 72
Coded by Raul Gonzalez
"""


class Problem72:
    def __init__(self, words_to_generate, initial_seed_value, length_of_words):
        self.CONSONANTS = "bcdfghjklmnprstvwxz"
        self.VOWELS = "aeiou"
        self.generated_words = list()
        self.words_to_generate = words_to_generate
        self.initial_seed_value = initial_seed_value
        self.length_of_words = length_of_words

    def solve(self):
        x0 = self.initial_seed_value
        for i in range(self.words_to_generate):
            string = ""
            for j in range(self.length_of_words[i]):
                x0 = (445*x0+700001) % 2097152
                if j % 2 == 0:
                    string += self.CONSONANTS[x0 % len(self.CONSONANTS)]
                else:
                    string += self.VOWELS[x0 % len(self.VOWELS)]
            self.generated_words.append(string)
        return " ".join(self.generated_words)

if __name__ == "__main__":
    num_words_to_generate, seed_value = map(int, input().split())
    word_lengths = list(map(int, input().split()))
    print(Problem72(num_words_to_generate, seed_value, word_lengths).solve())
