"""
CodeAbbey, Problem 24
Coded by whoisrgj
"""

N = int(input())
numbers = list(input().split())
results = set()
    
for num in numbers:
    iterations = 0
    results.add(num)
    while 1:
        iterations += 1
        result = str(int(num)**2).zfill(8)[2:6]
        if result not in results:
            results.add(result)
            num = int(result)
        else:
            break
    print(iterations, end=' ')
    results.clear()