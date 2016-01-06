from collections import Counter

def isValidWord(length, letters_count, letters_given, word):
	if(len(word) != length):
		return False
	word_letter_count = Counter()
	for c in word:
		word_letter_count[c] += 1
	for c in word:
		if word_letter_count[c] > letters_count[c]:
			return False
	return True

test_cases = int(input())
for i in range(test_cases):
	# get input
	letters_given = input().split()
	length = int(letters_given.pop(0))
	
	# count letters in input
	letters_count = Counter()
	for c in letters_given:
		letters_count[c] += 1
		
	# search for words
	words = list()
	f = open('words.txt', 'r')
	for line in f:
		word = line.rstrip()
		if isValidWord(length, letters_count, letters_given, word):
			words.append(word)
	#print(words)
	print(len(words), end=" ")