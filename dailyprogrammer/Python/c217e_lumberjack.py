"""
    reddit.com/r/dailyprogrammer
    Challenge #217 Easy
    Lumberjack Pile Problem
	https://redd.it/3840rp

    Solution by whoisrgj.
    http://www.whoisrgj.com
"""
 
row_size = int(input())
new_logs = int(input())
logs = []

for i in range(row_size):
   logs += list(map(int, input().split()))

for i in range(new_logs):
    logs[logs.index(min(logs))] += 1
            
for i in range(0, row_size*row_size, row_size):
    print(*logs[i:i+row_size])