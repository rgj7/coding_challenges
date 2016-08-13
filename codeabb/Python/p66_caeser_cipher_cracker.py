"""
CodeAbbey, Problem 66
Coded by whoisrgj
"""
from collections import deque, defaultdict
from string import ascii_uppercase


class CaeserCipherCracker(object):

    IDEAL_FREQUENCY = [
        8.1, 1.5, 2.8, 4.3, 13.0, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 7.0, 2.4,
        6.8, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]

    def __init__(self, encoded_string):
        self.encoded_string = encoded_string

    @staticmethod
    def _average_frequency(string):
        letters = [c for c in string if c in ascii_uppercase]
        letter_count = defaultdict(int)
        for c in letters:
            letter_count[c] += 1
        return [(letter_count[c] / len(letters)) * 100
                for c in ascii_uppercase]

    @staticmethod
    def _caesar_shift_cipher(s, k):
        shifted_letters = ascii_uppercase[k:] + ascii_uppercase[:k]
        table = s.maketrans(shifted_letters, ascii_uppercase)
        return s.translate(table)

    def _calculate_diff(self, real_freq):
        return sum(map(lambda x, y: (x-y)**2, real_freq, self.IDEAL_FREQUENCY))

    def decode(self):
        real_freq = deque(self._average_frequency(self.encoded_string))
        diffs = []
        for i in range(26):
            diffs.append((i, self._calculate_diff(real_freq)))
            real_freq.rotate(-1)
        key, _ = min(diffs, key=lambda t: t[1])
        return key, self._caesar_shift_cipher(self.encoded_string, key)


def main():
    n = int(input())
    results = []
    for _ in range(n):
        ccc = CaeserCipherCracker(input())
        key, decoded_string = ccc.decode()
        results.append(" ".join(decoded_string.split()[:3]))
        results.append(str(key))
    print(*results)


if __name__ == '__main__':
    main()
