"""
CodeAbbey, Problem 88
Coded by whoisrgj
"""


class NoteFrequency(object):
    NAMES = 'C C# D D# E F F# G G# A A# B'
    STEPS = {k: v for v, k in enumerate(NAMES.split())}

    @classmethod
    def calculate_frequency(cls, note: str):
        octave = int(note[-1])
        name = note[:-1]
        # in relation to A4
        half_steps = (cls.STEPS[name] - 9) + (octave - 4) * 12
        return round(440 * (2**(1/12)) ** half_steps)  # base A4


def main():
    n = int(input())  # not used
    notes = input().split()
    print(*(NoteFrequency.calculate_frequency(note) for note in notes))

if __name__ == '__main__':
    main()
