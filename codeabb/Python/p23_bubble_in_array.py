"""
CodeAbbey, Problem 23
Coded by whoisrgj
"""

def checksum(numbers, seed, limit):
    result = 0
    for i in numbers:
        result = ((result+i)*seed) % limit
    return result
    
numbers = list(map(int, input().split()))
numbers.pop() # remove -1 at end
swaps = 0
for i in range(1, len(numbers)):
    if numbers[i-1] > numbers[i]: # swap if greater
        numbers[i-1], numbers[i] = numbers[i], numbers[i-1] # swap
        swaps += 1;
print(swaps, checksum(numbers, 113, 10000007))