"""
CodeAbbey, Problem 127
Coded by whoisrgj
"""

from collections import defaultdict

try:
    wordlist = defaultdict(list)
    with open('words.txt', 'r') as file:
        for word in file.read().splitlines():
            word_sorted = "".join(sorted(word))
            wordlist[word_sorted].append(word)
except IOError as e:
    print("I/O Error({0}): {1}".format(e.errno, e.strerror))
    
N = int(input())
for tc in range(N):
    word = input()
    word_sorted = "".join(sorted(word))
    print(len([w for w in wordlist[word_sorted]])-1, end=' ')
