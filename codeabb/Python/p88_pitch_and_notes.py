"""
CodeAbbey, Problem 88
Coded by whoisrgj
"""

NOTE_STEPS = {k: v for v, k in enumerate('C C# D D# E F F# G G# A A# B'.split())}


def note_freq(note: str):
    name = note[:-1]
    octave = int(note[-1])
    half_steps = (NOTE_STEPS[name] - 9) + (octave - 4) * 12  # in relation to A4
    return round(440 * (2**(1/12)) ** half_steps)  # base A4


def main():
    int(input())  # not used
    notes = input().split()
    print(*(note_freq(note) for note in notes))

if __name__ == '__main__':
    main()
