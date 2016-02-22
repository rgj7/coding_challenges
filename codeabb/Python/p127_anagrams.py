"""
CodeAbbey, Problem 127
Coded by whoisrgj
"""


def anagram_count(word):
    count = -1  # accounts for original word
    word_sorted = "".join(sorted(word))
    with open('words.txt', 'r') as f:
        for line in f:
            test_word = line.rstrip()
            if len(word) == len(test_word) and word_sorted == "".join(sorted(test_word)):
                count += 1
    return count


def main():
    n = int(input())
    print(*(anagram_count(input()) for _ in range(n)))

if __name__ == '__main__':
    main()
