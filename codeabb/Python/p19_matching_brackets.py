"""
CodeAbbey, Problem 19
Coded by whoisrgj
"""

import time
start_time = time.time()

bracket_set = {'[':']','{':'}','<':'>','(':')'}
bracket_end = set(bracket_set.values())

N = int(input())

for tc in range(N):
    line = list(input())
    stack = []
    valid = True
    for c in line:
        if c in bracket_set:
            stack.append(c)
        elif c in bracket_end:
            if len(stack) == 0:
                valid = False
                break
            x = stack.pop()
            if bracket_set[x] != c:
                valid = False
                break
    if len(stack) > 0:
        valid = False
    print(int(valid), end=' ')
    
print("--- %s seconds ---" % (time.time() - start_time))
